from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
