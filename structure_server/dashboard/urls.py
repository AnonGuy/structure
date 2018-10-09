"""
Dashboard app URL Configuration.
"""

from dashboard import views

from django.urls import path


urlpatterns = [
    path("", views.HomePageView.as_view()),
    path("sign-in/", views.SignInView.as_view()),
]
