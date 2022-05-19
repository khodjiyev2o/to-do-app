from django.db import models

# Create your models here.


class Weather(models.Model):
    city = models.CharField(max_length=30)


    def __str__(self):
        return self.city


class Car(models.Model):
    carname = models.CharField(max_length=30)
    owner_phone = models.IntegerField()
    price = models.CharField(max_length=30)
    description=models.TextField()
    user=models.IntegerField(blank=False,default=1)
    photo=models.ImageField(upload_to='carsTreu/',blank=True,null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.carname



