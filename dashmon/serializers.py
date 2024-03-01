from rest_framework import serializers
from .models import Wifis


class WifisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wifis
        fields = ['ssid', 'channel', 'rssi']
