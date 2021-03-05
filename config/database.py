# db_setting
import os

DJANGO_COMPOSE = str(os.environ.get('DJANGO_COMPOSE', False)).lower() in ['true', '1']


if DJANGO_COMPOSE:
    setup = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DJANGO_DB_NAME', 'admin'),
            'USER': os.environ.get('DJANGO_DB_USERNAME', 'admin'),
            'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'adminadmin'),
            'HOST': os.environ.get('DJANGO_DB_HOST', 'database'),
            'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
        }
    }
else:
    DB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # You define your db sysetm with online or other container without django-compose
    setup = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DB_DIR, 'db.sqlite3'),
        }
    }
