from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')

# def catalog(request):
#     return render(request, 'main/catalog.html')