"""Dashboard view objects."""

from django.core import serializers

from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .scraper import valid_user
from .models import User, Student


class HomePageView(TemplateView):
    """HomePage view: default view of the landing page."""

    def get(self, request, *args, **kwargs):
        if request.session.get('authenticated'):
            return render(request, "dashboard.html", context=request.session)
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
        user = User(
            username=username, password=password
        )
        if valid_user(user):
            print('User validated!')
            existing_user = User.objects.filter(username=user.username).first()
            if existing_user:
                user = existing_user
            else:
                user.save()
            user = serializers.serialize('json', [user])
            request.session['user'] = user
            request.session['authenticated'] = True
            redirect('/')
        else:
            print('Incorrect credentials.')
            request.session['authenticated'] = False

        return render(request, "sign-in.html", context=None)
