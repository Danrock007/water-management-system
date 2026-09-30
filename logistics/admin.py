from django.contrib import admin

from .models import Driver, Vehicle, Delivery


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone_number',
        'license_number',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'phone_number',
        'license_number',
    )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):

    list_display = (
        'registration_number',
        'vehicle_type',
        'capacity',
        'is_active',
        'created_at',
    )

    list_filter = (
        'vehicle_type',
        'is_active',
    )

    search_fields = (
        'registration_number',
    )


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'driver',
        'vehicle',
        'status',
        'delivery_date',
        'is_active',
        'created_at',
    )

    list_filter = (
        'status',
        'is_active',
    )

    search_fields = (
        'order__order_number',
        'driver__name',
        'vehicle__registration_number',
    )
