from rest_framework import serializers

from .models import Animal, Feeder, Vaccination


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class FeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeder
        fields = '__all__'


class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = '__all__'