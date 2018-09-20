"""
Dashboard app URL Configuration.
"""

from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from dashboard import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('sign-in/', views.SignInView.as_view()),
]
