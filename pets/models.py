from django.db import models

class Pet(models.Model):
    SPECIES_CHOICES = [
        ('Cat', 'Kucing'),
        ('Dog', 'Anjing'),
        ('Other', 'Lainnya'),
    ]

    STATUS_CHOICES = [
        ('Available', 'Tersedia'),
        ('Adopted', 'Sudah Diadopsi'),
    ]

    name = models.CharField(max_length=100, verbose_name="Nama Hewan")
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES, verbose_name="Jenis")
    age = models.PositiveIntegerField(verbose_name="Umur (Bulan)", help_text="Umur dalam hitungan bulan")
    description = models.TextField(verbose_name="Deskripsi")
    photo = models.ImageField(upload_to='pets/', verbose_name="Foto Hewan", null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available', verbose_name="Status Adopsi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.species})"
