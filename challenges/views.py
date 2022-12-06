from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Not supported")
    redirect_month = months[month-1]
    return HttpResponseRedirect(reverse("month-challenge", args=[redirect_month]))


def monthly_challenge(request, month):
    response_text = monthly_challenges[month]
    response_data = f"<h1>{response_text}</h1>"
    return HttpResponse(response_data)
        