from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RoomInformationSerializer
from .models import RoomInformation


class PostList(generics.ListCreateAPIView):
    queryset = RoomInformation.postobjects.all()
    serializer_class = RoomInformationSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = RoomInformation.postobjects.all()
    serializer_class = RoomInformationSerializer