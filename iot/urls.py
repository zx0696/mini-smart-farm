from django.urls import path, include
from .views import *
from django.views.generic import TemplateView

app_name = 'iot'

urlpatterns = [ 
    path('mqtt/', TemplateView.as_view(template_name='iot/mqtt.html'), name='mqtt'),
]