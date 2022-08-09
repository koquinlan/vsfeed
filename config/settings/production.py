from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "vsfeed",
        "USER": "name",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}
