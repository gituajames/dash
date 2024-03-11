from django.db import models


class Wifis(models.Model):
    ssid = models.CharField(max_length=100)
    channel = models.IntegerField()
    rssi = models.IntegerField()


class PingTime(models.Model):
    ssid = models.CharField(max_length=100)
    ping_time = models.IntegerField()
