from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Knob sweep type options: A tuple of 2-tuples
SWEEP_TYPES = (
    ('C', 'Continuous'),
    ('D', 'Discrete')
)

class Guitar(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    year = models.IntegerField()
    serial_number = models.IntegerField()

    # Other goodness such as 'def __str__():' below
    def __str__(self):
        return f'{self.year} {self.color} {self.brand} {self.model}\n#{self.serial_number}'

    # Add this method
    def get_absolute_url(self):
        return reverse('guitar_detail', kwargs={'guitar_id': self.id})    
        # class Meta:
        #     ordering = ['-date']


class Pedal(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    amperage = models.IntegerField()
    voltage = models.IntegerField()
    guitars = models.ManyToManyField(Guitar)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def goes_to_11(self):
        return self.knob_set.filter(max_value=11).count() >= 1

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

class Photo(models.Model):
    url = models.CharField(max_length=200)
    pedal = models.ForeignKey(Pedal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pedal_id: {self.pedal_id} @{self.url}"