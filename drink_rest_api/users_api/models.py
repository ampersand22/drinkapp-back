from django.conf import settings
from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class UserAccount(models.Model):
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
