from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Workout twice a week!",
    "february": "Practice Django for at least 30 minutes every day!",
    "march": "Eat no fast food all month.",
    "april": "Drink no soda all month",
    "may": "Practice React for at least 30 minutes every day.",
    "june": "Eat no fast food all month.",
    "july": "Workout twice a week!",
    "august": "Practice Django for at least 30 minutes every day!",
    "september": "Eat no fast food all month.",
    "october": "Drink no soda all month",
    "november": "Practice React for at least 30 minutes every day.",
    "december": "Eat no candy all month."
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    try:
        redirect_month = months[month - 1]
        redirect_path = reverse("month_challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Invalid month entered.")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
