import os
import dj_database_url
from settings.base import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': dj_database_url.config(
            default=os.environ.get('DATABASE_URL')
            )
        }
    }

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ['EMAIL_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PW']
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = os.environ['EMAIL_DEFAULT']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ACCOUNT_ACTIVATION_DAYS = 3

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
