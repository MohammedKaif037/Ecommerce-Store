from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    
class products(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,max_length=100)
    pid_for_home=models.IntegerField(default='0')

    def __str__(self) -> str:
        return self.title

class  User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.CharField(max_length=200)

class ShippingInformation(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    ordered_item= models.CharField(max_length=150)

class PaymentInformation(models.Model):
    card_number = models.CharField(max_length=255)
    expiration_date = models.CharField(max_length=255)
    cvv = models.CharField(max_length=255,)
    billing_address = models.CharField(max_length=255)

class OrderInformation(models.Model):
    title=models.CharField(max_length=255)

