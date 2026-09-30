from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Driver, Vehicle, Delivery
from .serializers import (
    DriverSerializer,
    VehicleSerializer,
    DeliverySerializer,
)


class DriverViewSet(viewsets.ModelViewSet):

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]


class VehicleViewSet(viewsets.ModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]


class DeliveryViewSet(viewsets.ModelViewSet):

    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]