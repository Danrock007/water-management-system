from rest_framework import viewsets , serializers
from rest_framework.permissions import IsAuthenticated

from .models import Product, Supplier, StockTransaction
from .serializers import (
    ProductSerializer,
    SupplierSerializer,
    StockTransactionSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class StockTransactionViewSet(viewsets.ModelViewSet):
    queryset = StockTransaction.objects.all()
    serializer_class = StockTransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        product = serializer.validated_data['product']
        transaction_type = serializer.validated_data['transaction_type']
        quantity = serializer.validated_data['quantity']

        if transaction_type == StockTransaction.TransactionType.STOCK_OUT:

            if quantity > product.quantity_in_stock:
                raise serializers.ValidationError(
                    "Not enough stock available."
                )

        transaction = serializer.save()

        if transaction_type == StockTransaction.TransactionType.STOCK_IN:

            product.quantity_in_stock += quantity

        elif transaction_type == StockTransaction.TransactionType.STOCK_OUT:

            product.quantity_in_stock -= quantity

        elif transaction_type == StockTransaction.TransactionType.ADJUSTMENT:

            product.quantity_in_stock = quantity

        product.save()