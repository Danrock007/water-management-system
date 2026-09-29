from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            'Water System Information',
            {
                'fields': (
                    'role',
                    'phone_number',
                    'employee_id',
                )
            }
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Water System Information',
            {
                'fields': (
                    'role',
                    'phone_number',
                    'employee_id',
                )
            }
        ),
    )