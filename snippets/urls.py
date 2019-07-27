from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('<int:pk>/', views.SnippetDetail.as_view()),
    path('greeting', views.greeting, name='greeting'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
