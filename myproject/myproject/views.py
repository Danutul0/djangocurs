from django.shortcuts import render
import json

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')