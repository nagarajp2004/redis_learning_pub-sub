from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import redis

# Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

def publish_view(request):
    r.publish('mychannel', 'Hello from Django Pub!')
    return HttpResponse("Message published to Redis!")
