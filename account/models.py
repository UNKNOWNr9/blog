from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name='شماره تماس')

    class Meta:
        verbose_name = 'کابر'
        verbose_name_plural = 'کابران'
