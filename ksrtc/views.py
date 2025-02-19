from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import BusTrip
from .serializers import BusTripSerializer
from django.contrib.auth.models import User
from ksrtc.serializers import UserSerializer
from rest_framework import permissions

class BusTripViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,  
                     viewsets.GenericViewSet): 
     
    serializer_class = BusTripSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return BusTrip.objects.none()
        if user.is_superuser:
            return BusTrip.objects.all()  # Admins see all trips
        return BusTrip.objects.filter(user=user)  # Normal users see only their trips

    def list(self, request, *args, **kwargs):
        source = request.query_params.get('source', None)
        destination = request.query_params.get('destination', None)

        bus_trips = self.get_queryset()

        if source and destination:
            filtered_bus_trips = []
            for bus_trip in bus_trips:
                stations = bus_trip.stations
                source_index = next((index for index, station in enumerate(stations) if station['station'] == source), None)
                destination_index = next((index for index, station in enumerate(stations) if station['station'] == destination), None)

                if source_index is not None and destination_index is not None and destination_index > source_index:
                    filtered_bus_trips.append(bus_trip)

        elif source:
            # Only filter by source
            filtered_bus_trips = [bus_trip for bus_trip in bus_trips if any(station['station'] == source for station in bus_trip.stations)]
        elif destination:
            # Only filter by destination
            filtered_bus_trips = [bus_trip for bus_trip in bus_trips if any(station['station'] == destination for station in bus_trip.stations)]
        else:
            filtered_bus_trips = bus_trips 
        serializer = self.get_serializer(filtered_bus_trips, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = UserSerializer  