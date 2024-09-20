from pathlib import Path

from decouple import config
from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY', default='local-secret-key')
DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = []

INSTALLED_DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
INSTALLED_THIRD_PARTY_APPS = [
    'django_extensions',
    'ninja',
]
INSTALLED_LOCAL_APPS = [
    'api',
]
INSTALLED_APPS = INSTALLED_DJANGO_APPS + INSTALLED_THIRD_PARTY_APPS + INSTALLED_LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': config('DJANGO_DATABASE_DEFAULT', default='psql://sims:sims@db:5432/sims', cast=Env.db_url_config),
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': config('DJANGO_CACHE_DEFAULT', default='redis://cache:6379/0', cast=Env.cache_url_config),
    'auth': config('DJANGO_CACHE_AUTH', default='redis://cache:6379/1', cast=Env.cache_url_config),
    'lock': config('DJANGO_CACHE_LOCK', default='redis://cache:6379/2', cast=Env.cache_url_config),
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
