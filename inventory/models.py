from django.db import models


class Product(models.Model):

    class ProductType(models.TextChoices):
        SACHET_WATER = 'SACHET_WATER', 'Sachet Water'
        BOTTLED_WATER = 'BOTTLED_WATER', 'Bottled Water'
        DISPENSER_WATER = 'DISPENSER_WATER', 'Dispenser Water'
        OTHER = 'OTHER', 'Other'

    name = models.CharField(
        max_length=150
    )

    product_type = models.CharField(
        max_length=30,
        choices=ProductType.choices,
        default=ProductType.SACHET_WATER
    )

    description = models.TextField(
        blank=True
    )

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    quantity_in_stock = models.PositiveIntegerField(
        default=0
    )

    reorder_level = models.PositiveIntegerField(
        default=10
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


class Supplier(models.Model):

    name = models.CharField(
        max_length=150
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    address = models.TextField(
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
        return self.name    


class StockTransaction(models.Model):

    class TransactionType(models.TextChoices):
        STOCK_IN = 'STOCK_IN', 'Stock In'
        STOCK_OUT = 'STOCK_OUT', 'Stock Out'
        ADJUSTMENT = 'ADJUSTMENT', 'Adjustment'

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='stock_transactions'
    )

    transaction_type = models.CharField(
        max_length=20,
        choices=TransactionType.choices
    )

    quantity = models.PositiveIntegerField()

    reference = models.CharField(
        max_length=100,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type} - {self.quantity}"        