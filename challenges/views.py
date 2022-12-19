from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Not supported")
    redirect_month = months[month-1]
    return HttpResponseRedirect(reverse("month-challenge", args=[redirect_month]))


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
        })
    except:
        raise Http404()
        