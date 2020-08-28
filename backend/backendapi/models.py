from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.


# class Vendor(models.Model):
#     name = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     code = models.CharField(max_length=20, unique=True)
#     email = models.EmailField(blank=True)

class Stock(models.Model):
    size = models.CharField(max_length= 20,null=True)
    brand = models.CharField(max_length= 30, null=True)
    price = models.CharField(max_length=30,null=True)

    def __str__(self):
        return str(self.brand) if self.brand else ''
        return self.brand


class Order(models.Model):
    vendor = models.ForeignKey(Stock, default=1, on_delete = models.SET_NULL, null=True)
    name = models.CharField(max_length=50,null=True)
    number = models.CharField(max_length=150,null=True)
    address = models.CharField(max_length=50,null=True)
    size = models.CharField(max_length=50,null=True)
    note = models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.name


class Complaints(models.Model):
    order = models.ForeignKey(User, default=None, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50,null=True)
    body = models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.title

