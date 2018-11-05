"""Dashboard view objects."""

from django.core import serializers
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import User
from .scraper import LandingPageParser, valid_user


class HomePageView(TemplateView):
    """HomePage view: default view of the landing page."""

    def get(self, request, *args, **kwargs):
        if request.session.get('authenticated'):
            print('Authentication check successful!')
            user = next(serializers.deserialize(
                'json', request.session['user']
            ))
            parser = LandingPageParser(user.object)
            student = parser.parse().__dict__
            student.pop('_state')
            request.session['student'] = student
            return render(
                request, "dashboard.html", context=dict(request.session)
            )
        else:
            print('Authentication check failed...')
            return redirect("/sign-in")


class SignInView(TemplateView):
    """SignInView: view for the sign in page."""

    def get(self, request, *args, **kwargs):
        if request.session.get('authenticated'):
            return redirect('/')
        else:
            return render(request, "sign-in.html", context=None)

    def post(self, request):
        username, password = (
            request.POST.get('username'), request.POST.get('password')
        )
        user = User(username=username, password=password)
        if valid_user(user):
            print('User validated!')
            existing_user = User.objects.filter(username=user.username).first()
            if existing_user:
                user = existing_user
            user.save()
            user = serializers.serialize('json', [user])
            request.session['user'] = user
            request.session['authenticated'] = True
            print('Redirecting...')
            return redirect('/')
        else:
            print('Incorrect credentials.')
            request.session['authenticated'] = False

        return render(request, "sign-in.html", context=None)
