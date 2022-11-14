from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for all month")


def february(request):
    return HttpResponse("Meditation for 20 minutes")

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for all month"
    elif month == "february":
        challenge_text = "Meditation for 20 minutes"
    else:
        return HttpResponseNotFound("This month is not supported yet!")
    return HttpResponse(challenge_text)