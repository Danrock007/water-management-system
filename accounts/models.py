from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):
        ADMINISTRATOR = 'ADMINISTRATOR', 'Administrator'
        MANAGER = 'MANAGER', 'Manager'
        SALES_OFFICER = 'SALES_OFFICER', 'Sales Officer'
        WAREHOUSE_OFFICER = 'WAREHOUSE_OFFICER', 'Warehouse Officer'
        ACCOUNTANT = 'ACCOUNTANT', 'Accountant'
        DRIVER = 'DRIVER', 'Driver'

    role = models.CharField(
        max_length=30,
        choices=Role.choices,
        default=Role.SALES_OFFICER
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    employee_id = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
