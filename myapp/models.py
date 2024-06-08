from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


# Create your models here.

class Signuptable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='signuptable', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    place = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
class newproducts(models.Model):
    Image = models.ImageField()
    ProductName = models.CharField(max_length=1000,default="productname")
    Price = models.DecimalField(max_digits=10, decimal_places=2,default="productname")
    Brand = models.CharField(max_length=100, default="productname")
    Description = models.CharField(max_length=1000,default="productname")



    def __str__(self):
        return self.ProductName

class laptop(newproducts):
    pass

class accessories(newproducts):
    pass



class Carttable(models.Model):
    product_id = models.IntegerField(default=0)
    image = models.FileField()
    product_name = models.CharField(max_length=100, default='default')
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.CharField(max_length=100, default='default')

    def __str__(self):
        return self.product_name


class Billtable(models.Model):
    product_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=100, default='default')
    last_name = models.CharField(max_length=100, default='default')
    mobile = models.IntegerField(default=0)
    email = models.EmailField(max_length=100)
    date = models.DateField(default=timezone.now)
    product_name = models.CharField(max_length=100, default='default')
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField(default=0)



class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name