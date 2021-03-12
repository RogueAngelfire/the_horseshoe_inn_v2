from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RoomInformationSerializer
from .models import RoomInformation


@api_view(['GET'])
def room_inforamation(request):
    
    api_urls ={
        'List': '/room_information/'
    }
    
    return Response(api_urls)


@api_view(['GET'])
def room_information_list(request):
    room_information = RoomInformation.objects.all()
    serializer = RoomInformationSerializer(room_information, many=True)
    return Response(serializer.data)