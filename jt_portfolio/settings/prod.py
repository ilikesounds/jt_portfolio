import os
import dj_database_url
from jt_portfolio.settings.base import *


DEBUG = True

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(module)s %(message)s'
            },
        },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/logs/jtp.log',
            'maxBytes': 1024000,
            'backupCount': 3,
            },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
            }
        },
    'loggers': {
        'django': {
            'handlers': ['file', 'console', 'mail_admins'],
            'propagate': True,
            'level': 'DEBUG',
            },
        }
    }
