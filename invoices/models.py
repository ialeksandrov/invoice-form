from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name
