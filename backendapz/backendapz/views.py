from rest_framework.response import Response
from forestry.models import Animal, Feeder, Vaccination
from forestry.serializers import AnimalSerializer, FeederSerializer, VaccinationSerializer
from rest_framework.views import APIView


class FeederListView(APIView):
    def get(self, request):
        feeders = Feeder.objects.filter()
        serializer = FeederSerializer(feeders, many=True)
        return Response(serializer.data)


class AnimalsListView(APIView):
    def get(self, request):
        animals = Animal.objects.filter()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)
