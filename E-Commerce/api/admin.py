from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Product, Cart, CartItem, Order, OrderItem


# admin.site.register(User)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
