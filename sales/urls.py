from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, OrderViewSet , InvoiceViewSet


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

router.register(
    r'invoices',
    InvoiceViewSet,
    basename='invoices'
)

urlpatterns = [
    path('', include(router.urls)),
]
