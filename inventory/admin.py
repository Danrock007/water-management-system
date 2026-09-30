from django.contrib import admin
from .models import Product, Supplier, StockTransaction


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'product_type',
        'unit_price',
        'quantity_in_stock',
        'reorder_level',
        'is_active',
        'created_at',
    )

    list_filter = (
        'product_type',
        'is_active',
    )

    search_fields = (
        'name',
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone_number',
        'email',
        'is_active',
        'created_at',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'phone_number',
        'email',
    )


@admin.register(StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):

    list_display = (
        'product',
        'transaction_type',
        'quantity',
        'reference',
        'created_at',
    )

    list_filter = (
        'transaction_type',
        'created_at',
    )

    search_fields = (
        'product__name',
        'reference',
    )