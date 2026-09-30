from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, OrderViewSet


router = DefaultRouter()

router.register(
    r'customers',
    CustomerViewSet,
    basename='customers'
)

router.register(
    r'orders',
    OrderViewSet,
    basename='orders'
)


urlpatterns = [
    path('', include(router.urls)),
]
