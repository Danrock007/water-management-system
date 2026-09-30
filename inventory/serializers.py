from rest_framework import serializers

from .models import Product, Supplier, StockTransaction


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'product_type',
            'description',
            'unit_price',
            'quantity_in_stock',
            'reorder_level',
            'is_active',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = [
            'id',
            'name',
            'phone_number',
            'email',
            'address',
            'is_active',
            'created_at',
            'updated_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]


class StockTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockTransaction
        fields = [
            'id',
            'product',
            'transaction_type',
            'quantity',
            'reference',
            'notes',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
        ]