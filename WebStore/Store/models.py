from django.db import models

# Create your models here.
class kontakt(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=100)
    msg = models.CharField(max_length=1200)

class Product(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductPrice = models.CharField(max_length=100)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    Qua = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)