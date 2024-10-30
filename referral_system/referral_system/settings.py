import os
from datetime import timedelta
from decouple import config
from pathlib import Path


SECRET_KEY = config('DJANGO_SECRET_KEY', 'sgQYWxFmNR77f1svX4HB39Q8WzBw6DW0q6OIrio5C-aT84fPCak3Wu_qSaeuedjgJfE')
BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'referrals',  # наше приложение
    'drf_yasg',
]


# Настройка TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             BASE_DIR  / 'templates'
        ],
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

# Настройки базы данных (пример для MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'referral_db',
        'USER': 'Vigen0080',
        'PASSWORD': '0080',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Настройка JWT аутентификации
REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# Настройки MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Статические файлы и другие настройки
STATIC_URL = '/static/'
ROOT_URLCONF = 'referral_system.urls'
