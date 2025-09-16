from django.shortcuts import render
from django.http import HttpResponseServerError
from django.template import TemplateDoesNotExist

def index(request):
    try:
        return render(request, 'start/home.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found')

def citizen_login(request):
    try:
        return render(request, 'start/citizen_login.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found')

def citizen_register(request):
    try:
        return render(request, 'start/citizen_register.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found')

def department_login(request):
    try:
        return render(request, 'start/dep_login.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found')

def department_register(request):
    try:
        return render(request, 'start/dep_register.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found')