from django.shortcuts import render, get_object_or_404
from .models import Pet

def home(request):
    pets = Pet.objects.filter(status='Available').order_by('-created_at')
    return render(request, 'home.html', {'pets': pets})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pet_detail.html', {'pet': pet})
