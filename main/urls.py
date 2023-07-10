from django.urls import path, include
from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/main.html'), name='main'),
]


