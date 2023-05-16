# models.py
from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class ProductList(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_lists')

    def __str__(self):
        return self.name


class ProductEntry(models.Model):
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    product_list = models.ForeignKey(ProductList, related_name='entries', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
