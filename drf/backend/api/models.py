from django.db import models
import decimal


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=99.99)

    @property
    def sale_price(self):
        return round(self.price * 0.8,2)

    def get_discount(self):
        return round(self.price / 2, 2)
