from django.db import models

import uuid

from django.utils.translation import ugettext_lazy as _
from django.db import models
from accounts import models as user_models


class Feeder(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    PREDATOR = 'PR'
    HERBIVORE = 'HB'
    TYPE_CHOICES = (
        (PREDATOR, 'Predator'),
        (HERBIVORE, 'Herbivore')
    )
    type = models.CharField(max_length=2,
                            choices=TYPE_CHOICES,
                            default=HERBIVORE)
    forestry = models.ForeignKey(user_models.Forestry, on_delete=models.CASCADE)


class Animal(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('name'), max_length=100)
    vaccinated = models.BooleanField(_('vaccinated'))


class Vaccination(models.Model):
    id = models.UUIDField(_('id'), primary_key=True, default=uuid.uuid4, editable=False)
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE)
    created = models.DateTimeField(_('created'), auto_now_add=True)

    class Meta:
        ordering = ['-created']
