from django.shortcuts import render
from django.http import HttpResponse
from .pedals_list import pedals

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pedals_index(request):
  return render(request, 'pedals/index.html', { 'pedals': pedals })