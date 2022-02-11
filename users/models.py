from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    #nickname of users
    nickname = models.CharField(max_length=70,blank=True)
    class Meta(AbstractUser.Meta):
        pass

# Create your models here.
