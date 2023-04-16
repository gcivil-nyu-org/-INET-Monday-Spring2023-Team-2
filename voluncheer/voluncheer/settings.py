"""
Django settings for voluncheer project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

from voluncheer.environment import environment

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "insecure")

# Security
CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
]
_CSRF_TRUSTED_ORIGINS_CSV = os.getenv("CSRF_TRUSTED_ORIGINS_CSV")
if _CSRF_TRUSTED_ORIGINS_CSV:
    CSRF_TRUSTED_ORIGINS.extend(_CSRF_TRUSTED_ORIGINS_CSV.split(","))

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]
_ALLOWED_HOSTS_CSV = os.getenv("ALLOWED_HOSTS_CSV")
if _ALLOWED_HOSTS_CSV:
    ALLOWED_HOSTS.extend(_ALLOWED_HOSTS_CSV.split(","))

# Application definition
INSTALLED_APPS = [
    # Run server application
    "daphne",
    "gunicorn",
    # Django built-ins
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # External applications
    "crispy_forms",
    "crispy_bootstrap5",
    "storages",
    "channels",
    "supervisor",  # Not sure if supervisor is needed here.
    "channels_redis",
    "mathfilters",
    # Local applications
    "opportunityboard.apps.OpportunityboardConfig",
    "map.apps.MapConfig",
    "profiles.apps.ProfilesConfig",
    "chatroom.apps.ChatroomConfig",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "voluncheer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            (os.path.join(BASE_DIR, "templates")),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "voluncheer.wsgi.application"
ASGI_APPLICATION = "voluncheer.asgi.application"

if environment.is_aws:
    REDIS_CHATROOM_PORT = os.getenv("REDIS_CHATROOM_PORT")
else:
    REDIS_CHATROOM_PORT = "127.0.0.1"


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_CHATROOM_PORT, 6379)],
        },
    }
}


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
if environment.is_local:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("POSTGRES_HOST"),
            "PORT": os.getenv("POSTGRES_PORT"),
        },
    }

# Storage
# https://django-storages.readthedocs.io/en/latest
if environment.is_aws:
    AWS_S3_ACCESS_KEY_ID = os.getenv("AWS_S3_ACCESS_KEY_ID")
    AWS_S3_SECRET_ACCESS_KEY = os.getenv("AWS_S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/"
else:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# You can change the logic of determining whether or not the Debug Toolbar
# should be shown with the SHOW_TOOLBAR_CALLBACK option.
SHOW_TOOLBAR_CALLBACK = True

INTERNAL_IPS = [
    "127.0.0.1",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# Authentication and authorization
AUTH_USER_MODEL = "profiles.User"
LOGIN_URL = "login"
LOGOUT_URL = "logout"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
ACCOUNT_USERNAME_REQUIRED = False

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Backend Email
if environment.is_aws:
    EMAIL_BACKEND = "django_ses.SESBackend"
    AWS_ACCESS_KEY_ID = os.getenv("AWS_SES_ACCESS_KEY")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SES_SECRET_ACCESS_KEY")
    AWS_SES_REGION_NAME = os.getenv("AWS_SES_REGION_NAME")
    AWS_SES_REGION_ENDPOINT = os.getenv("AWS_SES_REGION_ENDPOINT")
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

AWS_SES_DOMAIN = os.getenv("AWS_SES_DOMAIN")
DEFAULT_FROM_EMAIL = os.getenv("AWS_SES_FROM_EMAIL")

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not environment.is_production

if DEBUG:
    INSTALLED_APPS.append("debug_toolbar")
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
    TEMPLATES[0].get("OPTIONS", {}).get("context_processors", []).append(
        "django.template.context_processors.debug"
    )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
if environment.is_local:
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    # STATIC_ROOT = os.path.join(BASE_DIR, "static")
else:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
