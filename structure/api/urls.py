"""API URL Configuration."""

from api import views

from django.urls import path


urlpatterns = [
    path("student-data", views.StudentDataView.as_view())
]
