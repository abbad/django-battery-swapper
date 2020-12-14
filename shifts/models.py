from django.db import models


class VehicleShift(models.Model):
    battery_swapped = models.BooleanField(default=False)
    
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.CASCADE)
    shift = models.ForeignKey('shifts.Shift', on_delete=models.CASCADE)

    def __str__(self):
        return F"VehicleShift: {self.id} Shift: {self.shift}"
    
    class Meta:
        unique_together = (("vehicle", "shift"),)


class Shift(models.Model):
    # This should be a forign key to user.
    user = models.CharField(max_length=255, unique=True)
    vehicles = models.ManyToManyField(through=VehicleShift, to='vehicles.Vehicle')

    def __str__(self):
        return F"id {self.id}"
