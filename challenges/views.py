from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for all month")


def february(request):
    return HttpResponse("Meditation for 20 minutes")