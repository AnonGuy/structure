"""structure_server URL Configuration."""

from django.urls import include, path

urlpatterns = [
    path("", include("dashboard.urls")),
    path("api/", include("api.urls"))
]
