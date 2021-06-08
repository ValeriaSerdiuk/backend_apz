from django.shortcuts import render

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from . import models
from .models import Forestry, Animal, Feeder, Vaccination
from .serializers import ForestrySerializer, AnimalSerializer, FeederSerializer, VaccinationSerializer


class ForestryViewSet(ModelViewSet):
    queryset = Forestry.objects.all()
    serializer_class = ForestrySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]


class FeederViewSet(ModelViewSet):
    queryset = Feeder.objects.all()
    serializer_class = FeederSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    permission_classes = [IsAuthenticated]


class VaccinationViewSet(ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    permission_classes = [IsAuthenticated]

