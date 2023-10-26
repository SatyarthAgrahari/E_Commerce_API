from django.db import models
from django.contrib.auth.models import User


# Model for category table
class Category(models.Model):
    name= models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
# Model for Product table
class Product(models.Model):
    name=models.CharField(max_length=50, blank=False,null=False)
    description=models.TextField(blank=False,null=False)
    price=models.DecimalField(max_digits=10,decimal_places=2, blank=False,null=False)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="products")
    image=models.ImageField(upload_to='products/',null=True,blank=True)

    def __str__(self):
        return self.name
    
# Model for cart table
class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=False,null=False)

# Model for CartItem table
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,blank=False,null=False)
    quantity=models.PositiveIntegerField(blank=False,null=False)

# Model for Order table
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    is_checked_out=models.BooleanField(default=False)

# Model for OrderItem table
class OrderItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=False,null=False)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,blank=False,null=False)
    quantity=models.PositiveIntegerField(blank=False,null=False)



