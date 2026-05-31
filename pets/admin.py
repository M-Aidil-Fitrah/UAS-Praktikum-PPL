from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'status', 'created_at')
    list_filter = ('species', 'status')
    search_fields = ('name', 'description')
    list_editable = ('status',)
