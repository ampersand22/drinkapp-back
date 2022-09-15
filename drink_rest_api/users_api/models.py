from email.policy import default
from django.db import models
# import uuid
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()


# Create your models here.
class UserAccount(models.Model):
    email = models.CharField(max_length=75, unique=True)
    password = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    id_user = models.IntegerField(default=0)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username + self
