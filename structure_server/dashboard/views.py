from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import User
from .scraper import valid_user


current_session: dict = {}


class HomePageView(TemplateView):
    """HomePage view: default view of the landing page."""

    def get(self, request, *args, **kwargs):
        if current_session.get('authenticated'):
            return render(request, "dashboard.html", context=current_session)
        else:
            return redirect("/sign-in")


class SignInView(TemplateView):
    """SignInView: view for the sign in page."""

    def get(self, request, *args, **kwargs):
        return render(request, "sign-in.html", context=None)

    def post(self, request):
        username, password = (
            request.POST.get('username'), request.POST.get('password')
        )
        user = User(username=username, password=password)
        if valid_user(user):
            current_session['user'] = user
            current_session['authenticated'] = True
            redirect('/')
        else:
            current_session['authenticated'] = False
        return render(request, "sign-in.html", context=None)
