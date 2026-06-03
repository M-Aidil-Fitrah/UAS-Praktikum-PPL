from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Pet
from .forms import PetForm, RegisterForm

def home(request):
    pets = Pet.objects.filter(status='Available')
    
    search_query = request.GET.get('q', '')
    if search_query:
        pets = pets.filter(name__icontains=search_query)
        
    species_query = request.GET.get('species', '')
    if species_query:
        pets = pets.filter(species=species_query)
        
    pets = pets.order_by('-created_at')
    
    context = {
        'pets': pets,
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
    if pet.status == 'Available':
        pet.status = 'Pending'
        pet.adopter = request.user
        pet.save()
    return redirect('pet_detail', pk=pk)

@login_required
def my_adoptions(request):
    pets = Pet.objects.filter(adopter=request.user).order_by('-updated_at')
    return render(request, 'my_adoptions.html', {'pets': pets})

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
    return render(request, 'dashboard/index.html', {'pets': pets})

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
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST' and pet.status == 'Pending':
        pet.status = 'Adopted'
        pet.save()
    return redirect('dashboard_index')

@staff_member_required(login_url='user_login')
def dashboard_reject_pet(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST' and pet.status == 'Pending':
        pet.status = 'Available'
        pet.adopter = None
        pet.save()
    return redirect('dashboard_index')


