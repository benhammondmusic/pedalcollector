from django.db import models
from django.urls import reverse

# Knob sweep type options: A tuple of 2-tuples
SWEEP_TYPES = (
    ('C', 'Continuous'),
    ('D', 'Discrete')
)


class Pedal(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    amperage = models.IntegerField()
    voltage = models.IntegerField()

    def goes_to_11(self):
        return self.knob_set.filter(max_value=11).count() >= 1
        # return whether or not any of the knobs on this pedal go to eleven (or more)
        # for knob in self.knob_set:
            # print (knob)
            # if knob.max_value  >= 11: return True
        # return False
        


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pedal_id': self.id})


class Knob(models.Model):
    setting_name = models.CharField('Setting Name',max_length=16)
    current_value = models.FloatField('Current Value')
    max_value = models.IntegerField('Max Value')
    sweep_type = models.CharField(max_length=1, choices=SWEEP_TYPES, default=SWEEP_TYPES[0][0])

    pedal = models.ForeignKey(Pedal, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_sweep_type_display()} {self.setting_name} knob: set to {self.current_value}/{self.max_value}"

