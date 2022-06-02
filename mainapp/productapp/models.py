from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    rcv_date = models.DateTimeField()
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    vendor_name = models.CharField(max_length=64)
