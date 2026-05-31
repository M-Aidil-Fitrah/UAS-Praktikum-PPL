from django.urls import path
from . import views

urlpatterns = [
    # Public URLs
    path('', views.home, name='home'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    
    # Dashboard URLs
    path('dashboard/login/', views.dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', views.dashboard_logout, name='dashboard_logout'),
    path('dashboard/', views.dashboard_index, name='dashboard_index'),
    path('dashboard/pet/add/', views.dashboard_pet_create, name='dashboard_pet_create'),
    path('dashboard/pet/edit/<int:pk>/', views.dashboard_pet_update, name='dashboard_pet_update'),
    path('dashboard/pet/delete/<int:pk>/', views.dashboard_pet_delete, name='dashboard_pet_delete'),
]
