from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),  # /challenges/
    path("<int:months>", views.MonthsInNumber),
    path("<str:months>", views.Months, name="month-challenge")
]
