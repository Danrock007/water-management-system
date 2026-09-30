from django.db import models


class Driver(models.Model):

    name = models.CharField(
        max_length=150
    )

    phone_number = models.CharField(
        max_length=20
    )

    license_number = models.CharField(
        max_length=50,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Vehicle(models.Model):

    class VehicleType(models.TextChoices):
        TRUCK = 'TRUCK', 'Truck'
        VAN = 'VAN', 'Van'
        MOTORBIKE = 'MOTORBIKE', 'Motorbike'
        OTHER = 'OTHER', 'Other'

    registration_number = models.CharField(
        max_length=30,
        unique=True
    )

    vehicle_type = models.CharField(
        max_length=20,
        choices=VehicleType.choices,
        default=VehicleType.TRUCK
    )

    capacity = models.PositiveIntegerField(
        help_text='Maximum number of units the vehicle can carry.'
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.registration_number  



class Delivery(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        ASSIGNED = 'ASSIGNED', 'Assigned'
        IN_TRANSIT = 'IN_TRANSIT', 'In Transit'
        DELIVERED = 'DELIVERED', 'Delivered'
        CANCELLED = 'CANCELLED', 'Cancelled'

    order = models.OneToOneField(
        'sales.Order',
        on_delete=models.PROTECT,
        related_name='delivery'
    )

    driver = models.ForeignKey(
        Driver,
        on_delete=models.PROTECT,
        related_name='deliveries'
    )

    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.PROTECT,
        related_name='deliveries'
    )

    delivery_address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    delivery_date = models.DateField(
        null=True,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.order.order_number} - {self.status}"
