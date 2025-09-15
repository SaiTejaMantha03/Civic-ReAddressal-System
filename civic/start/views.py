from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'start/home.html')

def citizen_login(request):
    return render(request, 'start/citizen_login.html')

def citizen_register(request):
    return render(request, 'start/citizen_register.html')

def dep_login(request):
    return render(request, 'start/dep_login.html')

def dep_register(request):
    return render(request, 'start/dep_register.html')