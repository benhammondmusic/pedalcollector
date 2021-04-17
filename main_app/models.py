from django.db import models
from django.urls import reverse

class Pedal(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    amperage = models.IntegerField()
    voltage = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pedal_id': self.id})
