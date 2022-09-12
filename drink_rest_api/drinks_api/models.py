from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=32)
    image = models.TextField()
    ingredients = models.CharField(max_length=255)
    comments = models.CharField(max_length=500)
    likes = models.IntegerField()
    location = models.CharField(max_length=64)
    tags = models.CharField(max_length=255)