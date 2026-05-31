from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
]
