from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from forestry.models import Forestry, Animal, Feeder, Vaccination
from forestry.serializers import ForestrySerializer, AnimalSerializer, FeederSerializer, VaccinationSerializer


@csrf_exempt
def forestry_list(request):
    if request.method == 'GET':
        fr = Forestry.objects.all()
        fr_serializer = ForestrySerializer(fr, many=True)
        return JsonResponse(fr_serializer.data, safe=False)

    elif request.method == 'POST':
        fr_data = JSONParser().parse(request)
        fr_serializer = ForestrySerializer(data=fr_data)

        if fr_serializer.is_valid():
            fr_serializer.save()
            return JsonResponse(fr_serializer.data,
                                status=201)
        return JsonResponse(fr_serializer.errors,
                            status=400)


@csrf_exempt
def forestry_detail(request, pk):
    try:
        fr = Forestry.objects.get(pk=pk)
    except Forestry.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        fr_serializer = ForestrySerializer(fr)
        return JsonResponse(fr_serializer.data)
    elif request.method == 'DELETE':
        fr.delete()
        return HttpResponse(status=204)


@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = 'server is live current time is '
    return Response(data=message + date, status=status.HTTP_200_OK)