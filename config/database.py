# db_setting
DBSET = 'DEV'

if DBSET == 'LIVE':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DJANGO_DB_NAME', 'orderplus'),
            'USER': os.environ.get('DJANGO_DB_USERNAME', 'orderplus'),
            'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'x_x@212ho.com'),
            'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),
            'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DJANGO_DB_NAME', 'orderplus'),
            'USER': os.environ.get('DJANGO_DB_USERNAME', 'orderplus'),
            'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'x_x@212ho.com'),
            'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),
            'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
        }
    }
