from django.contrib import admin
from .models import Customer , Order , Invoice


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'customer_type',
        'phone_number',
        'email',
        'is_active',
        'created_at',
    )

    list_filter = (
        'customer_type',
        'is_active',
    )

    search_fields = (
        'name',
        'phone_number',
        'email',
    )


    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'customer',
        'status',
        'total_amount',
        'is_active',
        'created_at',
    )

    list_filter = (
        'status',
        'is_active',
    )

    search_fields = (
        'order_number',
        'customer__name',
    )

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'invoice_number',
        'order',
        'amount',
        'status',
        'due_date',
        'is_active',
        'created_at',
    )

    list_filter = (
        'status',
        'is_active',
    )

    search_fields = (
        'invoice_number',
        'order__order_number',
    )
