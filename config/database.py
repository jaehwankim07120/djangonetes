# db_setting
DBSET = 'DEV'

if DBSET == 'LIVE':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ople',
            #'NAME': 'ople_test',
            'USER': 'ople',
            'PASSWORD': 'ohmysql@x_x.co.kr',
            'HOST': 'ople-db.koreacentral.cloudapp.azure.com',
            'PORT': '5000',
            'OPTIONS': {
                'connect_timeout': 240,
                'init_command': 'SET storage_engine=InnoDB',
            },
            # 0: closing the database connection at the end of each request. should lower than 240
            'CONN_MAX_AGE': 0
        },
        'settlebank': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'settlebank',
            'USER': 'ople',
            'PASSWORD': 'ohmysql@x_x.co.kr',
            'HOST': 'ople-db.koreacentral.cloudapp.azure.com',
            'PORT': '5000',
        },
        'salesforce': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'salesforce',
            'USER': 'ople',
            'PASSWORD': 'x_x@song2ro',
            'HOST': 'datatest.koreacentral.cloudapp.azure.com',
            'PORT': '5000',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'ople',
            # 'NAME': 'ople_test',*
            'USER': 'ople',
            'PASSWORD': 'ohmysql@x_x.co.kr',
            'HOST': 'opledev.koreacentral.cloudapp.azure.com',
            'PORT': '5000',
            'OPTIONS': {
                'connect_timeout': 240,
            },
            'CONN_MAX_AGE': 0
        },
        'settlebank': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'settlebank',
            'USER': 'ople',
            'PASSWORD': 'ohmysql@x_x.co.kr',
            'HOST': 'opledev.koreacentral.cloudapp.azure.com',
            'PORT': '5000',
        },
        'salesforce': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'salesforce',
            'USER': 'ople',
            'PASSWORD': 'x_x@song2ro',
            'HOST': 'datatest.koreacentral.cloudapp.azure.com',
            'PORT': '5000',
        }
    }

'''
Service DB
{
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', 'orderplus'),
        'USER': os.environ.get('DJANGO_DB_USERNAME', 'orderplus'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', 'x_x@212ho.com'),
        'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'),
    }
}
'''
