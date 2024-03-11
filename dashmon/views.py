from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Wifis, PingTime
from .serializers import WifisSerializer, PingTimeSerializers


@api_view(['GET'])
def getdata(request):
    data = Wifis.objects.all()
    serializer = WifisSerializer(data, many=True)
    return Response(serializer.data)


def index(request):
    return HttpResponse("dashh")


@api_view(['POST'])
def postdata(request):
    serializer = WifisSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response(serializer.data)


def show_status(request):
    wifi_status = Wifis.objects.all().order_by("-date_time")[:5]
    pingtimes = PingTime.objects.all()
    context = {
        'wifi_status': wifi_status,
        'pingtimes': pingtimes,
    }
    return render(request, 'dash.html', context)


@api_view(['POST'])
def postpingtime(request):
    serializer = PingTimeSerializers(data=request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
        return Response(serializer.data)
# Create your views here.
