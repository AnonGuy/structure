"""
My own implementation of the Authentication backend.
Since my passwords need to be recoverable, this authentication system tries to
decrypt the password based on a padded 128-Bit AES key, which is derived from
the requester's public IP Address.
"""

from django.contrib.auth.backends import ModelBackend

from structure_server.dashboard.scraper import valid_user


class AuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return False
        return valid_user(username, password)
