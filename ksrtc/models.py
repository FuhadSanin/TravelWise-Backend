from django.db import models

class BusTrip(models.Model):
    vehicle_number = models.CharField(max_length=100, unique=True)
    trip = models.PositiveIntegerField()  # Trip number
    stations = models.JSONField(default=list)  # Stores list of stations with times

    def __str__(self):
        return f"Trip {self.trip} - {self.vehicle_number}"