"""Define various webscraping methods."""

import requests
from threading import Thread

from .models import User, Student


endpoint = "https://my.loreto.ac.uk/"


class LandingPageParser:
    """Class for parsing the Loreto landing page."""

    def __init__(self, user: User):
        response = requests.get(endpoint, auth=(user.username, user.password))
        self.page: str = response.content.decode()

    # TODO: Implement Threaded asset retrieval.


def valid_user(user: User) -> bool:
    """Take a User object and validate credentials."""
    print('Validating user...')
    return requests.get(
        endpoint, auth=(user.username, user.password)
    ).status_code == 200


def create_student(user: User) -> Student:
    """Take a User object and intialize a Student object."""
    pass

