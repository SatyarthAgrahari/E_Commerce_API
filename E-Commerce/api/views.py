from django.shortcuts import render
from .serializers import CategorySerializer,ProductSerializer,CartItemSerializer,OrderItemSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Category,Product,Cart,CartItem,Order,OrderItem

# Category View
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

# Product View
class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    # Add Validation for name
    def create(self, request, *args, **kwargs):
        if request.data.get('name')=="InvalidName":
            return Response({"error":"Invalid Product Name Provided."},status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
# CertItem View
class CartItemViewset(viewsets.ModelViewSet):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer

    def create(self, request, *args, **kwargs):
        if int(request.data.get('quantity',0))>10:
            return Response({"error": "Cannot add more than 10 items of the same product to the cart."}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)
    
#OrderItem View
class OrderItemViewset(viewsets.ModelViewSet):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer


