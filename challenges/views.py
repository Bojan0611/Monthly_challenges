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

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)
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
        return HttpResponseNotFound("<h1>Not supported</h1>")
        