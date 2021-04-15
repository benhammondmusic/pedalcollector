from django.db import models

class Pedal(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    amperage = models.IntegerField()
    voltage = models.IntegerField()

    def __str__(self):
        return self.name
