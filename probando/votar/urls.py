from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('votar/',views.index),
    path('una/',views.votar),
]