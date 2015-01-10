from base import *
import os

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'catalog',
        'USER': os.getenv('OPENSHIFT_MYSQL_DB_USER'),
        'PASSWORD': os.getenv('OPENSHIFT_MYSQL_DB_PASS'),
        'HOST': os.getenv('OPENSHIFT_MYSQL_DB_HOST'),
        'PORT': os.getenv('OPENSHIFT_MYSQL_DB_PORT')
    }
}