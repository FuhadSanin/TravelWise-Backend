from django import forms
from .models import BusTrip

class BusTripForm(forms.ModelForm):
    class Meta:
        model = BusTrip
        fields = ['vehicle_number', 'trip', 'stations']