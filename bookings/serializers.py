from rest_framework import serializers
from .models import RoomInformation


class RoomInformationSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = RoomInformation
        fields =  (
            'id',
            'room_name',
            'room_image',
            'room_description',
            'room_type',
            'room_ratings',
            'room_price_per_night')
        
    
