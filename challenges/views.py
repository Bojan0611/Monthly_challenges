from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for all month",
    "february": "Meditation for 20 minutes",
    "march": "Eat no meat for all month",
    "april": "Meditation for 20 minutes",
    "may": "nothing",
    "june": "Eat no meat for all month",
    "july": "Meditation for 20 minutes",
    "august": "Eat no meat for all month",
    "september": "Meditation for 20 minutes",
    "october": "Eat no meat for all month",
    "november": "Meditation for 20 minutes",
    "december": "go to the gym",
}

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("Not supported")