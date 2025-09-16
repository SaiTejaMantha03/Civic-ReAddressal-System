from django.shortcuts import render
from django.http import HttpResponseServerError
from django.template import TemplateDoesNotExist

def index(request):
    try:
        return render(request, 'ui/index.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found')

def status(request):
    try:
        return render(request, 'ui/status.html')
    except TemplateDoesNotExist:
        return HttpResponseServerError('Template not found')