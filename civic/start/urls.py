from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.citizen_login, name='citizen_login'),
    path('register/', views.citizen_register, name='citizen_register'),
    path('department_login/', views.department_login, name='department_login'),
    path('department_register/', views.department_register, name='department_register'),
]