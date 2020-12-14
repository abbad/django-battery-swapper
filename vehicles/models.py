from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

class Vehicle(models.Model):
    NIU = 'Niu'
    
    MODEL_CHOICES = [
        (1, NIU),
    ]

    # attributes 
    license_plate = models.CharField(unique=True, blank=False, max_length=255)
    
    battery_level = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], blank=False)

    in_use = models.BooleanField(default=False)

    # This can be a forign key to a Model/Make table. 
    model = models.IntegerField(choices=MODEL_CHOICES, blank=False, default=1)

    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False)

    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False)

    def __str__(self):
        return F"ID: {self.id}, License Plate: {self.license_plate}"
