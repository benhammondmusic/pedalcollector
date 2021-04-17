from django.forms import ModelForm
from .models import Knob

class KnobForm(ModelForm):
  class Meta:
    model = Knob
    fields = ['setting_name', 'current_value', 'max_value', 'sweep_type']
