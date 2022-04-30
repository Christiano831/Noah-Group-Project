from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Patient

# Create your views here.

def home (request):
    return HttpResponse ('working so far')

def about (request):
    # return HttpResponse('<h1> This is the About page </h1>')
    return render(request, 'about.html')

def patients_index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', {'patients': patients})