from django.urls import path, include
# from django.views.generic import TemplateView
from .views import *

app_name = 'data'

urlpatterns = [
    # path('graph/', TemplateView.as_view(template_name='data/graph.html'), name='graph'),
    path('graph/', graph, name='graph'),
    path('predict/', predict, name='predict'),
]


