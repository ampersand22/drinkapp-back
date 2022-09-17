from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=32)
    image = models.TextField()
    ingredients = models.CharField(max_length=255)
    comments = models.CharField(max_length=500)
    likes = models.IntegerField()
    locationDisplayName = models.CharField(max_length=64)
    address = models.CharField(max_length=200, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, null=True)
    tags = models.CharField(max_length=255)