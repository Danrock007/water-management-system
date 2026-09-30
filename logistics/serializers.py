from rest_framework import serializers

from .models import Driver, Vehicle, Delivery


class DriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver

        fields = [
            'id',
            'name',
            'phone_number',
            'license_number',
            'is_active',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle

        fields = [
            'id',
            'registration_number',
            'vehicle_type',
            'capacity',
            'is_active',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery

        fields = [
            'id',
            'order',
            'driver',
            'vehicle',
            'delivery_address',
            'status',
            'delivery_date',
            'notes',
            'is_active',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]