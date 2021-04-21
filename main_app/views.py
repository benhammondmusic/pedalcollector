from django.http import HttpResponse
from .models import Pedal, Guitar
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import KnobForm
from django.shortcuts import render, redirect
# from .pedals_list import pedals

# load up from database
def pedals_index(request):
  pedals = Pedal.objects.all()
  return render(request, 'pedals/index.html', { 'pedals': pedals })


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def add_knob(request, pedal_id):
  form = KnobForm(request.POST)
  if form.is_valid():
    # don't save the form to the db until it
    # has the pedal_id assigned
    new_knob = form.save(commit=False)
    new_knob.pedal_id = pedal_id
    new_knob.save()
  return redirect('detail', pedal_id=pedal_id)



# Pedals views

def pedals_detail(request, pedal_id):
  pedal = Pedal.objects.get(id=pedal_id)
  unmatched_guitars = Guitar.objects.exclude(id__in = pedal.guitars.all().values_list('id'))
  knob_form = KnobForm()
  context = { 'pedal': pedal, 'knob_form': knob_form, "guitars": unmatched_guitars }
  return render(request, 'pedals/detail.html', context)

class PedalCreate(CreateView):
  model = Pedal
  fields = '__all__'

class PedalUpdate(UpdateView):
  model = Pedal
  # Let's disallow renaming by excluding the name field!
  fields = ['brand', 'description', 'style', 'amperage', 'voltage']

class PedalDelete(DeleteView):
  model = Pedal
  success_url = '/pedals/'

# Guitars views

def guitars_index(request):
    guitars = Guitar.objects.all()
    context = {'guitars': guitars}
    
    return render(request, 'guitar/index.html', context)


def guitar_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    context = {
        'guitar': guitar
    }
    return render(request, 'guitar/detail.html', context)
    
class Create_Guitar(CreateView):
    model = Guitar
    fields = '__all__'


class Update_guitar(UpdateView):
    model = Guitar
    fields = ["brand", "model", "color", "year"]

class Delete_guitar(DeleteView):
    model = Guitar
    success_url = '/guitars/'     

def assoc_guitar(request, pedal_id, guitar_id):
  # Note that you can pass a guitar's id instead of the whole object
  Pedal.objects.get(id=pedal_id).guitars.add(guitar_id)
  return redirect('detail', pedal_id=pedal_id)


