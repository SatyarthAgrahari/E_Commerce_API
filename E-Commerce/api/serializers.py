from rest_framework import serializers
from .models import Category,Product,Cart,CartItem,Order,OrderItem


#Category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer()

    class Meta:
        model=Product
        fields='__all__'

    # Field Level Validation here field is price.
    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

# CartItem serializer    
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields='__all__'

        # Field Level Validation here field is quantity
        def validate_quantity(self,value):
            if value <= 0:
                raise serializers.ValidationError("Quantity must be greater than zero.")
            return value
        
# OrderItem serializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'

        # Field Level Validation here field is quantity
        def validate_quantity(self,value):
            if value<=0:
                raise serializers.ValidationError("Quantity must be greater than zero")
            
        

    
