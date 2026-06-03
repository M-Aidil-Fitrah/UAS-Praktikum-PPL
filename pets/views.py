from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Pet, AdoptionRequest, UserProfile
from .forms import PetForm, RegisterForm, AdoptionRequestForm, UserProfileForm

def home(request):
    pets = Pet.objects.filter(status='Available')
    
    search_query = request.GET.get('q', '')
    if search_query:
        pets = pets.filter(name__icontains=search_query)
        
    species_query = request.GET.get('species', '')
    if species_query:
        pets = pets.filter(species=species_query)
        
    pets = pets.order_by('-created_at')
    
    paginator = Paginator(pets, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'pets': page_obj,
        'page_obj': page_obj,
        'search_query': search_query,
        'species_query': species_query,
        'species_choices': Pet.SPECIES_CHOICES
    }
    return render(request, 'home.html', context)

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

@login_required
def adopt_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if pet.status != 'Available':
        messages.error(request, "Maaf, hewan ini tidak tersedia untuk diadopsi saat ini.")
        return redirect('pet_detail', pk=pk)
        
    if request.method == 'POST':
        form = AdoptionRequestForm(request.POST)
        if form.is_valid():
            adoption_req = form.save(commit=False)
            adoption_req.pet = pet
            adoption_req.user = request.user
            adoption_req.save()
            
            # Ubah status hewan menjadi pending
            pet.status = 'Pending'
            pet.adopter = request.user
            pet.save()
            
            messages.success(request, "Pengajuan adopsi berhasil dikirim! Menunggu persetujuan admin.")
            return redirect('my_adoptions')
    else:
        form = AdoptionRequestForm()
        
    return render(request, 'adopt_form.html', {'form': form, 'pet': pet})

@login_required
def my_adoptions(request):
    pets = Pet.objects.filter(adopter=request.user).order_by('-updated_at')
    return render(request, 'my_adoptions.html', {'pets': pets})

@login_required
def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil berhasil diperbarui!')
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)
        
    return render(request, 'profile.html', {'form': form})

# --- Custom Dashboard Views ---

def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('dashboard_index')
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('dashboard_index')
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@staff_member_required(login_url='user_login')
def dashboard_index(request):
    pets = Pet.objects.all().order_by('-created_at')
    paginator_pets = Paginator(pets, 10)
    page_number_pets = request.GET.get('page')
    page_obj_pets = paginator_pets.get_page(page_number_pets)
    
    pending_requests = AdoptionRequest.objects.filter(status='Pending').order_by('-created_at')
    paginator_req = Paginator(pending_requests, 10)
    page_number_req = request.GET.get('req_page')
    page_obj_req = paginator_req.get_page(page_number_req)
    
    return render(request, 'dashboard/index.html', {
        'pets': page_obj_pets, 
        'pending_requests': page_obj_req,
        'page_obj_pets': page_obj_pets,
        'page_obj_req': page_obj_req
    })

@staff_member_required(login_url='user_login')
def dashboard_pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_index')
    else:
        form = PetForm()
    return render(request, 'dashboard/pet_form.html', {'form': form, 'title': 'Tambah Hewan'})

@staff_member_required(login_url='user_login')
def dashboard_pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('dashboard_index')
    else:
        form = PetForm(instance=pet)
    return render(request, 'dashboard/pet_form.html', {'form': form, 'title': 'Edit Hewan'})

@staff_member_required(login_url='user_login')
def dashboard_pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('dashboard_index')
    return render(request, 'dashboard/pet_confirm_delete.html', {'pet': pet})

@staff_member_required(login_url='user_login')
def dashboard_approve_pet(request, pk):
    req = get_object_or_404(AdoptionRequest, pk=pk)
    if request.method == 'POST' and req.status == 'Pending':
        req.status = 'Approved'
        req.save()
        
        pet = req.pet
        pet.status = 'Adopted'
        pet.save()
        messages.success(request, f"Adopsi {pet.name} oleh {req.user.username} disetujui.")
    return redirect('dashboard_index')

@staff_member_required(login_url='user_login')
def dashboard_reject_pet(request, pk):
    req = get_object_or_404(AdoptionRequest, pk=pk)
    if request.method == 'POST' and req.status == 'Pending':
        req.status = 'Rejected'
        req.save()
        
        pet = req.pet
        pet.status = 'Available'
        pet.adopter = None
        pet.save()
        messages.error(request, f"Adopsi {pet.name} oleh {req.user.username} ditolak.")
    return redirect('dashboard_index')


