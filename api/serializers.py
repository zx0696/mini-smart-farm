from rest_framework import serializers
from iot.models import *

class EnvironmentalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentalData
        fields = ('id', 
                  'time', 
                  'temp', 
                  'humi', 
                  'co2', 
                  'water_supply', 
                  'water_supply_cumulative', 
                  'light', 
                  'light_cumulative', 
                  'soil_moisture1', 
                  'soil_moisture2', 
                  'soil_moisture3')

class PlantWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantWeight
        fields = ('id', 'date', 'weight')

class WaterLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterLevel
        fields = ('id', 'time', 'waterlevel')


