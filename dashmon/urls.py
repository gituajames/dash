from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import postdata, index, getdata, show_status
urlpatterns = [
    path('getdata', getdata, name='test'),
    # path('postd', csrf_exempt(postdata), name='postdata'),
    path('postd', postdata, name='postdata'),
    path('dash', show_status, name='show_status')
]
