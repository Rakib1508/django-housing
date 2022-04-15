from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get('DEBUG')) == "1" # 1 == True

ALLOWED_HOSTS = []
if not DEBUG:
    ALLOWED_HOSTS += [os.environ.get('DJANGO_ALLOWED_HOST')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {},
    'auth_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('AUTH_DB_NAME'),
        'USER': os.environ.get('AUTH_DB_USER'),
        'PASSWORD': os.environ.get('AUTH_DB_PASSWORD'),
        'HOST': os.environ.get('AUTH_DB_HOST'),
        'PORT': os.environ.get('AUTH_DB_PORT'),
    },
    'app_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('APP_DB_NAME'),
        'USER': os.environ.get('APP_DB_USER'),
        'PASSWORD': os.environ.get('APP_DB_PASSWORD'),
        'HOST': os.environ.get('APP_DB_HOST'),
        'PORT': os.environ.get('APP_DB_PORT'),
    },
    'dynamic_db': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get('DYNAMIC_DB_NAME'),
        'ENFORCE_SCHEMA': str(os.environ.get('DYNAMIC_DB_ENFORCE_SCHEMA')) == "1",
        'CLIENT': {
            'host': os.environ.get('DYNAMIC_DB_HOST'),
            'port': int(os.environ.get('DYNAMIC_DB_PORT')),
            'username': os.environ.get('DYNAMIC_DB_USER'),
            'password': os.environ.get('DYNAMIC_DB_PASSWORD'),
            'authSource': os.environ.get('DYNAMIC_DB_AUTH_SOURCE'),
            'authMechanism': os.environ.get('DYNAMIC_DB_AUTH_MECHANISM')
        },
        'LOGGING': {
            'version': int(os.environ.get('DYNAMIC_DB_VERSION')),
            'loggers': {
                'djongo': {
                    'level': os.environ.get('DYNAMIC_DB_DEBUG_LEVEL'),
                    'propagate': str(os.environ.get('DYNAMIC_DB_PROPAGATE')) == "1",                        
                }
            },
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
