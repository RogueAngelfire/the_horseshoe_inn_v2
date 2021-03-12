from django.shortcuts import render
from django.http import JsonResponse


def room_inforamation(request):
    return JsonResponse("API BASE POINT", safe=False)
