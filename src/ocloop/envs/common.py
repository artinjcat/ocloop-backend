import os
from pathlib import Path
from datetime import timedelta
from decouple import config  # type: ignore
from .local_setting import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SALT")



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',

    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',

    'channels',

    # check user agent(for device check)
    'django_user_agents',

    'auth.users',
    # 'accounts',
    # 'musics',
    # 'subscription',
    # 'players',
    # 'playlists',
    # 'helps',
    # 'searches',
    # 'events',
    # 'ocloop_versions',
    # 'packages',
    # 'apps.platforms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # check user agent(for device check)
    'django_user_agents.middleware.UserAgentMiddleware',
    # custom middleware
    'ocloop.middlewares.accept_ranges_middleware.AcceptRangesMiddleware'
]

ROOT_URLCONF = 'ocloop.urls.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'playlists.context_processors.playlist',
            ],
        },
    },
]

WSGI_APPLICATION = 'ocloop.wsgi.application'
ASGI_APPLICATION = 'ocloop.asgi.application'


# Password validation
# https://docs.djangoproject.com/en/6.1/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/6.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_ROOT = '/vol/web/static'
if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / 'static']
    STATIC_URL = 'static/'
    MEDIA_URL = f'{BASE_URL}media/'
    # MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'data/web/media')
    MEDIA_ROOT = '/vol/web/media'
else:
    STATICFILES_DIRS = [BASE_DIR / 'static']
    STATIC_URL = 'static/'
    MEDIA_URL = 'media/'
    MEDIA_ROOT = '/vol/web/media'



# Email
# https://docs.djangoproject.com/en/6.1/topics/email/#topic-email-configuration
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'core.authentication.rest_framework_auth.HybridJWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    # "TOKEN_OBTAIN_SERIALIZER": "accounts.serializers.custom_serializers.WithEmailTokenObtainPairSerializer",
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
}



SPECTACULAR_SETTINGS = {
    'TITLE': 'OCLoop API',
    'DESCRIPTION': 'OCLoop API',
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}


SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"


CSRF_COOKIE_HTTPONLY = False  # چون نیاز داریم از JS بخونیمش
CSRF_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SAMESITE = "Lax"


