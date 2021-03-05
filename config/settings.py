"""
Django settings for djangonetes project.
"""

import os
from config import database

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '7ngkdjajhzi2oi+6izsv+!hg5lhdhzb0(d8d(qv11$i=)14n*)')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get('DJANGO_DEBUG', True)).lower() in ['true', '1']


ALLOWED_HOSTS = []

if DEBUG:
    ALLOWED_HOSTS += ['*', ]
else:
    if str(os.environ.get('DJANGO_MODE_FREE_HOST', True)).lower() in ['true', '1']:
        ALLOWED_HOSTS += ['*', ]



# Application definition
DJANGO_APPS = [
    'jet.dashboard',
    'jet',
]

DJANGO_CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SERVICE_APPS = [
    'service'
]

REST_APPS = [
    'drf_yasg',      
    'rest_framework',
]


INSTALLED_APPS = []
INSTALLED_APPS += DJANGO_APPS
INSTALLED_APPS += DJANGO_CORE_APPS
INSTALLED_APPS += SERVICE_APPS
INSTALLED_APPS += REST_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
DATABASES = database.setup

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Kubernetes
FORCE_SCRIPT_NAME = str(os.environ.get('FORCE_SCRIPT_NAME', ''))

# Static & Media files (CSS, JavaScript, Images)
WHITENOISE_STATIC_PREFIX = str(os.environ.get('WHITENOISE_STATIC_PREFIX', '/static/'))
STATIC_URL = FORCE_SCRIPT_NAME + WHITENOISE_STATIC_PREFIX


STATIC_DIR = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]

STATIC_ROOT = os.path.join(ROOT_DIR,'.static_root')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
