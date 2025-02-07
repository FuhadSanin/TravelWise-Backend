from rest_framework import serializers
from .models import BusTrip

class BusTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTrip
        fields = '__all__'  # Include all fields