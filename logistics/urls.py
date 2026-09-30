from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    DriverViewSet,
    VehicleViewSet,
    DeliveryViewSet,
)


router = DefaultRouter()


router.register(
    r'drivers',
    DriverViewSet,
    basename='drivers'
)


router.register(
    r'vehicles',
    VehicleViewSet,
    basename='vehicles'
)


router.register(
    r'deliveries',
    DeliveryViewSet,
    basename='deliveries'
)


urlpatterns = [
    path('', include(router.urls)),
]