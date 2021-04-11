from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def Months(request, months):
    challenge_text = None
    if months == 'january':
        challenge_text = "This is january"
    elif months == 'february':
        challenge_text = "This is february"
    elif months == 'march':
        challenge_text = "This is march"
    else:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challenge_text)
