from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

class CustomerItems(models.Model):
    item_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    item_description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    value = models.IntegerField()
