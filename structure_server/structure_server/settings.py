"""Django settings for the structure_server project."""

import base64
import os

import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = """
Good practice for Django Applications suggest that secret keys should not be
defined as hard-coded strings in the settings.py file.
"""
SECRET_KEY = os.environ.get(
    "STRUCTURE_KEY", base64.b64encode(SECRET_KEY.encode()).decode()
)

DEBUG = True

ALLOWED_HOSTS = [
    'structure-server.herokuapp.com',
    '127.0.0.1',
    'localhost'
]


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "dashboard",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "structure_server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "structure_server.wsgi.application"


# Database {{{

DB_USER = os.environ.get("DB_USER") or "structure_admin"
PASSWORD = os.environ.get("STRUCTURE_ADMIN_PASSWORD")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "StructureDB",
        "USER": DB_USER,
        "PORT": "5432",
    }
}

if os.environ.get('DATABASE_URL') is not None:
    DATABASES["default"] = dj_database_url.config(
        conn_max_age=600, ssl_require=True
    )

if PASSWORD is not None:
    DATABASES["default"].update({"PASSWORD": PASSWORD})

# }}}

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_L10N = True

USE_TZ = True


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
