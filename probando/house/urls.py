from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('house/',views.index),
    path('votar/',views.votar),
]