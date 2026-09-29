from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'employee_id',
            'phone_number',
            'role',
            'is_active',
            'date_joined',
        ]

        read_only_fields = [
            'id',
            'date_joined',
        ]
