from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Wifis
from .serializers import WifisSerializer


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
    wifi_status = Wifis.objects.all()
    context = {
        'wifi_status': wifi_status
    }
    return render(request, 'dash.html', context)



# Create your views here.
