from django.http import HttpResponse
from django.shortcuts import render

from . import urls


def index(request):
    context = {'example_list': ['a01',
                                'a02',
                                'a03',
                                'a04',
                                'a05',
                                'a06',
                                'a07',
                                'a08',
                                'a09',
                                'a10',
                                'a11',
                                'a12',
                                'a13',
                                ]}
    return render(request, '/'.join([urls.app_name,'index.html']), context)


def a01(request):
    # 1부터 100까지 합 구하기

    # 1)
    #sum = 0
    #for i in range(1, 101):
    #    sum += i

    # 2)
    from functools import reduce
    sum = reduce(lambda x, y: x + y, range(1, 101))

    return HttpResponse('a01: {}'.format(sum))


def a02(request):
    return HttpResponse('a02')


def a03(request):
    return HttpResponse('a03')


def a04(request):
    return HttpResponse('a04')


def a05(request):
    return HttpResponse('a05')


def a06(request):
    return HttpResponse('a06')


def a07(request):
    return HttpResponse('a07')


def a08(request):
    return HttpResponse('a08')


def a09(request):
    return HttpResponse('a09')


def a10(request):
    return HttpResponse('a10')


def a11(request):
    return HttpResponse('a11')


def a12(request):
    return HttpResponse('a12')


def a13(request):
    return HttpResponse('a13')

