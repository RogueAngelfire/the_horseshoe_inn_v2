from rest_framework import serializers
from .models import RoomInformation


class RoomInformationSerializer(serializers.ModelSerializer):
        class Meta:
            model = RoomInformation
            fields = '__all__'
