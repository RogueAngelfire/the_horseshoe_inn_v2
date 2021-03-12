from django.urls import path
from . import views

urlpatterns = [
    path('room_inforamation/', views.room_inforamation, name='room_inforamation'),
    path('room_information_list/', views.room_information_list, name='room_information_list'),
    path('room_information_detail/<int:id>', views.room_information_detail, name='room_information_detail'),
    path('room_information_create/', views.room_information_create, name='room_information_create'),
]