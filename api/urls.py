from rest_framework import routers
from api.views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register('EnvironmentalData', EnvironmentalDataViewSet)
router.register('PlantWeight', PlantWeightViewSet)
router.register('WaterLevel', WaterLevelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


