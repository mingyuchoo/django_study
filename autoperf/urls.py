from django.urls import path

from autoperf import views


app_name = 'autoperf'
urlpatterns = [
    path('', views.index, name='index'),
    path('json_string', views.json_string, name='json_string'),
    path('yaml_string', views.yaml_string, name='yaml_string'),
]