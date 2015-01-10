from project.settings.base import * # noqa
import dj_database_url
import os

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES['default'] = dj_database_url.config()
