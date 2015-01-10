"""
WSGI config for catalog project.
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(get_wsgi_application())
