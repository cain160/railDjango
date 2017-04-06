import django
from django.db import models


# Create your models here.

class Position(models.Model):
    longitude = models.DecimalField(decimal_places=3,max_digits=10, default=0.0)
    latitude = models.DecimalField(decimal_places=3,max_digits=10, default=0.0)

    def __str__(self):
        return str(self.longitude)+'°L '+str(self.latitude)+'°l'

#    def latitude(self):
#        return self.latitude

#    def longitude(self):
#        return self.longitude


class Device(models.Model):
    distance_on = models.DecimalField("Distance covered while the device is active",decimal_places=4,max_digits=8)
    status = models.BooleanField("True if the device is on, and false otherwise")
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    speed = models.FloatField()

    def __str__(self):
        return str(self.position)+'  '+str(self.speed)+'m/s '+str(self.status)

    def path_taken(self):
        return self

    def last_position(self):
        return self


class Path(models.Model):
    coord = models.ForeignKey(Position)
    device = models.ForeignKey(Device)
    date = models.DateField(auto_now=True)


