from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
