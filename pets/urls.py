from django.urls import path
from . import views

urlpatterns = [
    # Public URLs
    path('', views.home, name='home'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    
    # Auth URLs
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
    
    # Buyer URLs
    path('adopt/<int:pk>/', views.adopt_pet, name='adopt_pet'),
    path('my-adoptions/', views.my_adoptions, name='my_adoptions'),
    
    # Dashboard URLs
    path('dashboard/', views.dashboard_index, name='dashboard_index'),
    path('dashboard/pet/add/', views.dashboard_pet_create, name='dashboard_pet_create'),
    path('dashboard/pet/edit/<int:pk>/', views.dashboard_pet_update, name='dashboard_pet_update'),
    path('dashboard/pet/delete/<int:pk>/', views.dashboard_pet_delete, name='dashboard_pet_delete'),
    path('dashboard/pet/approve/<int:pk>/', views.dashboard_approve_pet, name='dashboard_approve_pet'),
    path('dashboard/pet/reject/<int:pk>/', views.dashboard_reject_pet, name='dashboard_reject_pet'),
]
