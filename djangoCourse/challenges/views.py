from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "This is january",
    "february": "This is february",
    "march": "This is march",
    "april": "This is april",
    "may": "This is may",
    "june": "This is june",
    "july": "This is july",
    "august": "This is august",
    "september": "This is september"
}


# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # <li> <a href="..."> January</a></li>
    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def MonthsInNumber(reques, months):
    number_of_month = list(monthly_challenges.keys())

    if months > len(number_of_month):
        return HttpResponseNotFound(error_res)

    redirect_month = number_of_month[months-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def Months(request, months):
    try:
        challenge_text = monthly_challenges[months]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(error_res)


error_res = f"<h1> Invalid Month <h1>"
