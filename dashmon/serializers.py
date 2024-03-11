from rest_framework import serializers
from .models import Wifis, PingTime


class WifisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wifis
        fields = ['ssid', 'channel', 'rssi']


class PingTimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PingTime
        fields = ['ssid', 'ping_time']
