import email
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

class myUser(AbstractUser):
    name = models.CharField(max_length = 200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=13, null=True)
    gender = models.CharField(max_length=6, null=True)
    birthday = models.DateField(null=True)
# Create your models here.
