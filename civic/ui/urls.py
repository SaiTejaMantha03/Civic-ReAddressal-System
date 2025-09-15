from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='citizen_dashboard'),
    path('status/', views.status, name='citizen_status'),
]
