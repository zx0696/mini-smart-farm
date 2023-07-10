from django.db import models

class EnvironmentalData(models.Model):          # 환경정보
    time = models.DateTimeField()               # 측정 날짜-시간
    temp = models.FloatField()                  # 온도
    humi = models.FloatField()                  # 습도
    co2 = models.FloatField()                   # 이산화탄소
    water_supply= models.FloatField()           # 시간당 수분공급량
    water_supply_cumulative = models.FloatField()     # 누적 수분공급량
    light = models.FloatField()                 # 광량
    light_cumulative = models.FloatField()      # 누적 광량
    soil_moisture1 = models.FloatField()         # 토양 수분1
    soil_moisture2 = models.FloatField()         # 토양 수분2
    soil_moisture3 = models.FloatField()         # 토양 수분3

class PlantWeight(models.Model):      # 식물 무게
    date = models.DateTimeField()
    weight = models.FloatField()

class WaterLevel(models.Model):         # 수위
    time = models.DateTimeField()
    waterlevel = models.FloatField()


