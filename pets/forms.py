from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'description', 'photo', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2'}),
            'species': forms.Select(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2'}),
            'age': forms.NumberInput(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2'}),
            'description': forms.Textarea(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2', 'rows': 4}),
            'photo': forms.FileInput(attrs={'class': 'w-full text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-orange-50 file:text-orange-700 hover:file:bg-orange-100 cursor-pointer'}),
            'status': forms.Select(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2'}),
        }

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2'})

from .models import AdoptionRequest

class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['reason', 'experience']
        widgets = {
            'reason': forms.Textarea(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2', 'rows': 4, 'placeholder': 'Ceritakan alasan Anda ingin mengadopsi hewan ini...'}),
            'experience': forms.Textarea(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2', 'rows': 3, 'placeholder': 'Apakah Anda pernah memelihara hewan sebelumnya? Jika ya, ceritakan sedikit.'}),
        }

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'avatar']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2', 'placeholder': 'Contoh: 081234567890'}),
            'address': forms.Textarea(attrs={'class': 'w-full rounded-lg border-gray-300 shadow-sm focus:border-orange-500 focus:ring-orange-500 px-4 py-2', 'rows': 3, 'placeholder': 'Alamat lengkap tempat tinggal Anda'}),
            'avatar': forms.FileInput(attrs={'class': 'w-full text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-orange-50 file:text-orange-700 hover:file:bg-orange-100 cursor-pointer'}),
        }


