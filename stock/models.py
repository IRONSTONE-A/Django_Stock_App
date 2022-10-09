from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class UpdateCreate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=30)
    
class Product(UpdateCreate):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, releted_name="b_products")
    stock = models.SmallIntegerField(blank=True, null=True)
