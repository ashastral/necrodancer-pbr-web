import os

DEBUG = True

ENVIRONMENT = 'dev'

ALLOWED_HOSTS = ['pbr.example.com']

ADMINS = (,)

SERVER_EMAIL = 'pbr@example.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.example.com'
EMAIL_HOST_USER = 'pbr@example.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX='[pbr] '

TIME_ZONE = 'America/Phoenix'
USE_TZ = True

SECRET_KEY = 'random characters'

BASE_URL = 'https://pbr.example.com/'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
