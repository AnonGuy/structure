"""API view objects, for communication with the mobile app."""

from base64 import b64decode
import re

from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

from dashboard.models import User
from scraper import LandingPageParser, valid_user


class StudentDataView(TemplateView):
    """StudentDataView: provide student data, given basic authorization."""

    def get(self, request):
        return HttpResponse(
            '<p style="font-family: monospace">'
            '    These are not the HTTP methods you are looking for.'
            '</p>'
        )

    def post(self, request):
        basic_auth = request.META.get(
            'HTTP_AUTHORIZATION', ''
        )
        if re.match('Basic [A-Za-z0-9]', basic_auth):
            auth = basic_auth.partition(' ')[2]
            username, _, password = b64decode(auth).decode().partition(':')
            print(username, password)
            user = User(username=username, password=password)
            if valid_user(user):
                parser = LandingPageParser(user)
                student = parser.parse().__dict__
                student.pop('_state')
                return JsonResponse(student)
            else:
                return JsonResponse({}, status=400)
        else:
            return JsonResponse({}, status=400)
