from django.urls import path

from . import views


app_name = 'algorithm'
urlpatterns = [
    path('', views.index, name='index'),
    path('a01', views.a01, name='a01'),
    path('a02', views.a02, name='a02'),
    path('a03', views.a03, name='a03'),
    path('a04', views.a04, name='a04'),
    path('a05', views.a05, name='a05'),
    path('a06', views.a06, name='a06'),
    path('a07', views.a07, name='a07'),
    path('a08', views.a08, name='a08'),
    path('a09', views.a09, name='a09'),
    path('a10', views.a10, name='a10'),
    path('a11', views.a11, name='a11'),
    path('a12', views.a12, name='a12'),
    path('a13', views.a13, name='a13'),
]