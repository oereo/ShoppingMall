from django.db import models
from order.models import OrderItem
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    category = models.CharField(max_length=30, required=True)
    category_description = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Product(models.Model):
    product = models.OneToOneField(OrderItem, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d', blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.product
