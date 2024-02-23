from pathlib import Path
import os
from dotenv import load_dotenv
import uuid
import boto3
from botocore.client import Config

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-o+(7^na(9!jwfi9ch6#8%7zfnu-q+1ao^yjp!cw%+whbc*7c2o'

DEBUG = True

ALLOWED_HOSTS = ['*']
DJANGO_ALLOWED_HOSTS = ['*']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'fpages',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'sign',
    'protect',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'storages',
    'django_filters',
    'django_celery_results',
    'django_crontab',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewPortal_v2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'news.context_processors.real_time',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewPortal_v2.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

CSRF_TRUSTED_ORIGINS = ['http://mrGerber91-test-site-9dfe.twc1.net']
CORS_ALLOWED_ORIGINS = ['http://mrGerber91-test-site-9dfe.twc1.net']

SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 587  # Или 465
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'dj.news.ango@mail.ru'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = 'dj.news.ango@mail.ru'

STATIC_URL = 'http://a43db249-afcba5da-f823-48df-ae33-bb246aacb9e9.s3.timeweb.cloud/'

AWS_STORAGE_BUCKET_NAME = 'a43db249-afcba5da-f823-48df-ae33-bb246aacb9e9'
AWS_ACCESS_KEY_ID = 'PVLTOFQ8MRXLF05LLMEM'
AWS_SECRET_ACCESS_KEY = '8mnrUcoDV5YF7Z0KQD3WI2TeCxjCx0gWEr0DtLDz'
AWS_S3_ENDPOINT_URL = 'http://s3.timeweb.cloud'
AWS_S3_REGION_NAME = 'ru-1'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.timeweb.cloud'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_DIRS = [BASE_DIR / 'static']

BUCKET = 'a43db249-afcba5da-f823-48df-ae33-bb246aacb9e9'
FILENAME = 'sample.txt'

s3 = boto3.client(
    's3',
    endpoint_url='https://s3.timeweb.cloud',
    region_name='ru-1',
    aws_access_key_id='PVLTOFQ8MRXLF05LLMEM ',
    aws_secret_access_key='8mnrUcoDV5YF7Z0KQD3WI2TeCxjCx0gWEr0DtLDz',
)
