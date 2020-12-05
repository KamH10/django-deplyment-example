"""
Django settings for regprj1 project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os       # s20e148 added

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")      # s20e148 added
STATIC_DIR = os.path.join(BASE_DIR, "static")           # s20e148 added
MEDIA_DIR = os.path.join(BASE_DIR, "media")             # s20e148 added

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@e(42&hliqbdbj4&l#@bp*ijqmeokr0ia7)pd-7afv5bvoocwl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['kamtj.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',         # **NOTE** Make sure it's there
    'django.contrib.auth',          # **NOTE** Make sure it's there
    'django.contrib.contenttypes',  # **NOTE** Make sure it's there
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'regapp1',                      # **NOTE** s20e148 added
    # 'regapp1.apps.BasicAppConfig',
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

ROOT_URLCONF = 'regprj1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],    # **NOTE** s20e148 added TEMPLATE_DIR
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

WSGI_APPLICATION = 'regprj1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),   # **NOTE** s20e148 added
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators


# **NOTE** s20e148 added
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# **NOTE** pay attention
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{ 'min_length':9 },   # **NOTE** s20e148 added
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [ STATIC_DIR, ]              # s20e148 added

MEDIA_URL = '/media/'                           # s20e148 added
# MEDIA_ROOT = [ MEDIA_DIR, ]                   # s20e148 added
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    # s20e148 added

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("x BASE_DIR: ", BASE_DIR)             # \s20e154\regprj1
print("x TEMPLATE_DIR: ", TEMPLATE_DIR)     # \s20e154\regprj1\templates
print("x STATIC_DIR: ", STATIC_DIR)         # \s20e154\regprj1\static
print("x MEDIA_DIR: ", MEDIA_DIR)           # \s20e154\regprj1\media
print("x MEDIA_ROOT", MEDIA_ROOT)           # \s20e154\regprj1\media
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxx")

LOGIN_URL = '/regapp1/user_login/'
