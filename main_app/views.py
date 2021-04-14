from django.shortcuts import render
from django.http import HttpResponse
from .pedals_list import pedals

# Define the home view
def home(request):
  return HttpResponse('<h1>Pedal Collector</h1>')

def about(request):
  return render(request, 'about.html')

def pedals_index(request):
  return render(request, 'pedals/index.html', { 'pedals': pedals })