from django.db import models
import decimal


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    completed = models.BooleanField(default=False, blank=True, null=True)

