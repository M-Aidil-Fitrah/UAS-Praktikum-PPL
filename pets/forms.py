from django import forms
from .models import Pet

BASE_INPUT = 'w-full text-sm transition'
BASE_FILE  = 'w-full text-sm transition'

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'description', 'photo', 'status']
        widgets = {
            'name':        forms.TextInput(attrs={'class': BASE_INPUT, 'placeholder': 'Nama hewan'}),
            'species':     forms.Select(attrs={'class': BASE_INPUT}),
            'age':         forms.NumberInput(attrs={'class': BASE_INPUT, 'placeholder': 'Umur dalam bulan'}),
            'description': forms.Textarea(attrs={'class': BASE_INPUT, 'rows': 4, 'placeholder': 'Deskripsi singkat tentang hewan ini'}),
            'photo':       forms.FileInput(attrs={'class': BASE_FILE}),
            'status':      forms.Select(attrs={'class': BASE_INPUT}),
        }

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': BASE_INPUT, 'placeholder': 'Username (Maks 30 karakter)'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': BASE_INPUT, 'placeholder': 'Nama Depan'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': BASE_INPUT, 'placeholder': 'Nama Belakang'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': BASE_INPUT, 'placeholder': 'Alamat Email'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': BASE_INPUT})
            field.help_text = ''  # Clear default help texts to save space
            field.widget.attrs.update({'placeholder': ' '})

from .models import AdoptionRequest

class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['reason', 'experience']
        widgets = {
            'reason':     forms.Textarea(attrs={'class': BASE_INPUT, 'rows': 4, 'placeholder': 'Ceritakan alasan Anda ingin mengadopsi hewan ini...'}),
            'experience': forms.Textarea(attrs={'class': BASE_INPUT, 'rows': 3, 'placeholder': 'Apakah Anda pernah memelihara hewan sebelumnya?'}),
        }

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address', 'avatar']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': BASE_INPUT, 'placeholder': 'Contoh: 081234567890'}),
            'address':      forms.Textarea(attrs={'class': BASE_INPUT, 'rows': 3, 'placeholder': 'Alamat lengkap tempat tinggal Anda'}),
            'avatar':       forms.FileInput(attrs={'class': BASE_FILE}),
        }
