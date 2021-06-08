from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = ['username', 'phone']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


class Forestry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField('title', max_length=160, unique=True)
    name_of_owner = models.CharField('name_of_owner', max_length=100)
    city = models.CharField('city', max_length=100)
    population = models.IntegerField('population')
