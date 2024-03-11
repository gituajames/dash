from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import postdata, index, getdata, show_status, postpingtime
urlpatterns = [
    path('getdata', getdata, name='test'),
    # path('postd', csrf_exempt(postdata), name='postdata'),
    path('postd', postdata, name='postdata'),
    path('postpingtime', postpingtime, name='postpingtime'),
    path('dash', show_status, name='show_status')
]
