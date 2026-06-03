from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('Cat', 'Kucing'),
        ('Dog', 'Anjing'),
        ('Other', 'Lainnya'),
    ]

    STATUS_CHOICES = [
        ('Available', 'Tersedia'),
        ('Pending', 'Menunggu Persetujuan'),
        ('Adopted', 'Sudah Diadopsi'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nama Hewan")
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES, verbose_name="Jenis")
    age = models.PositiveIntegerField(verbose_name="Umur (Bulan)", help_text="Umur dalam hitungan bulan")
    description = models.TextField(verbose_name="Deskripsi")
    photo = models.ImageField(upload_to='pets/', verbose_name="Foto Hewan", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available', verbose_name="Status Adopsi")
    adopter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='adoptions', verbose_name="Pengadopsi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.species})"

class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Menunggu Persetujuan'),
        ('Approved', 'Disetujui'),
        ('Rejected', 'Ditolak'),
    ]

    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_requests', verbose_name="Hewan")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests', verbose_name="Pengadopsi")
    reason = models.TextField(verbose_name="Alasan Mengadopsi", help_text="Mengapa Anda ingin mengadopsi hewan ini?")
    experience = models.TextField(verbose_name="Pengalaman Memelihara Hewan", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', verbose_name="Status Pengajuan")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pengajuan {self.pet.name} oleh {self.user.username}"
