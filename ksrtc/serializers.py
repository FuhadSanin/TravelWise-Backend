from rest_framework import serializers
from .models import BusTrip
from django.contrib.auth.models import User


class BusTripSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True) 
    class Meta:
        model = BusTrip
        fields = ['id', 'vehicle_number', 'trip', 'stations', 'user']
        extra_kwargs = {'user': {'read_only': True}}  # Prevent manual assignment of the user

    def create(self, validated_data):
        request = self.context.get('request')  # Get request context
        if request and request.user and request.user.is_authenticated:
            validated_data['user'] = request.user  # Set user to authenticated user
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_superuser']  # Include only these fields

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user