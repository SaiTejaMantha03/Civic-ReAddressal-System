from django.shortcuts import render
from django.http import HttpResponseServerError
from django.template import TemplateDoesNotExist

def index(request):
    try:
        return render(request, 'dep/home.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found')
