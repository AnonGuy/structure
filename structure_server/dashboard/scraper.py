"""Define various webscraping methods."""

import requests

from .models import User


endpoint = "https://my.loreto.ac.uk/"


def valid_user(user: User) -> bool:
    """Take a User object and validate credentials."""
    print('Validating user...')
    return requests.get(
        endpoint, auth=(user.username, user.password)
    ).status_code == 200
