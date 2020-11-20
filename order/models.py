from django.db import models
from account.models import User
from product.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')



