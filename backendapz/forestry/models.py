from django.db import models

import uuid

from django.utils.translation import ugettext_lazy as _
from django.db import models


class Forestry(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('title'), max_length=160, unique=True)
    name_of_owner = models.CharField(_('name_of_owner'), max_length=100)
    city = models.CharField(_('city'), max_length=100)
    population = models.IntegerField(_('population'))


class Feeder(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    completed = models.BooleanField(_('completed'))
    forestry = models.ForeignKey('Forestry', on_delete=models.CASCADE)


class Animal(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('name'), max_length=100)
    weight = models.IntegerField(_('weight'))
    vaccinated = models.BooleanField(_('vaccinated'))
    feeder = models.ForeignKey('Feeder', on_delete=models.CASCADE)


class Vaccination(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        ordering = ['-created']


