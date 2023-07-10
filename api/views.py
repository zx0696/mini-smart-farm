from rest_framework import viewsets
from rest_framework.response import Response

from iot.models import *
from .serializers import *

class EnvironmentalDataViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentalData.objects.all().order_by('-id')  
    serializer_class = EnvironmentalDataSerializer  

class PlantWeightViewSet(viewsets.ModelViewSet):
    queryset = PlantWeight.objects.all().order_by('-id')  
    serializer_class = PlantWeightSerializer  

class WaterLevelViewSet(viewsets.ModelViewSet):
    queryset = WaterLevel.objects.all().order_by('-id')  
    serializer_class = WaterLevelSerializer  


