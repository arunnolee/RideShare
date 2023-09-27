from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerUserModel(AbstractUser):
    username = models.CharField(max_length=100,  unique= True)
    email = models.EmailField(unique= True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
