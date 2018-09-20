from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """HomePage view: default view of the landing page."""
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, 'dashboard.html', context=None)
        else:
            return redirect('/sign-in')


class SignInView(TemplateView):
    """SignInView: view for the sign in page."""
    def get(self, request, *args, **kwargs):
        return render(request, 'sign-in.html', context=None)

    def post(self, request):
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        return render(request, 'sign-in.html', context=None)
