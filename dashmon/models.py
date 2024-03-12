from django.db import models


class Wifis(models.Model):
    ssid = models.CharField(max_length=100)
    channel = models.IntegerField()
    rssi = models.IntegerField()
    date_time = models.DateTimeField(auto_now=True)


class PingTime(models.Model):
    ssid = models.CharField(max_length=100)
    ping_time = models.FloatField(default=0.0)
    ping_date_time = models.DateTimeField(auto_now=True)
