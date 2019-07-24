from django.shortcuts import render
from .settings import INSTALLED_APPS

from django.http import (
    Http404, HttpResponse,
)


def index(request):
    app_list = [item.split('.')[0] for item in INSTALLED_APPS if 'Config' in item]
    app_list.append('admin')

    context = {
        'app_list': app_list
    }
    return render(request, 'index.html', context)
