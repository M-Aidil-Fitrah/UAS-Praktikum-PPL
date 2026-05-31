from django.shortcuts import render, get_object_or_404
from .models import Pet

def home(request):
    pets = Pet.objects.filter(status='Available').order_by('-created_at')
    return render(request, 'home.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})

# --- Custom Dashboard Views ---
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .forms import PetForm

def dashboard_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard_index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_index')
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})

@login_required
def dashboard_logout(request):
    logout(request)
    return redirect('home')

@staff_member_required(login_url='dashboard_login')
def dashboard_index(request):
    pets = Pet.objects.all().order_by('-created_at')
    return render(request, 'dashboard/index.html', {'pets': pets})

@staff_member_required(login_url='dashboard_login')
def dashboard_pet_create(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_index')
    else:
        form = PetForm()
    return render(request, 'dashboard/pet_form.html', {'form': form, 'title': 'Tambah Hewan'})

@staff_member_required(login_url='dashboard_login')
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

@staff_member_required(login_url='dashboard_login')
def dashboard_pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'POST':
        pet.delete()
        return redirect('dashboard_index')
    return render(request, 'dashboard/pet_confirm_delete.html', {'pet': pet})

