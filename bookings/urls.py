from django.urls import path
from . import views

urlpatterns = [
    path('room_inforamation/', views.room_inforamation, name='room_inforamation'),
]