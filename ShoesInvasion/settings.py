"""
Django settings for ShoesInvasion project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from ensurepip import version
import os
from pathlib import Path

import pymysql
pymysql.install_as_MySQLdb()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^4ck*1pvbxsh2z_8z-_-**r!ye1^851+g^)i3gtyjk#8+e62v!'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DEBUG = True

ALLOWED_HOSTS = ['188.166.238.172','127.0.0.1']
# ALLOWED_HOSTS = ['188.166.238.172']


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.messages',
    'ShoesInvasionApp.apps.ShoesInvasionAppConfig',
    'ShoesInvasionAdmin.apps.ShoesInvasionAdminConfig',
    'ShoesInvasionEditor.apps.ShoesInvasionEditorConfig',
    'django_jenkins',
    'django_forms_bootstrap',
    'bootstrap4',
    'crispy_forms',
    'django.contrib.staticfiles', 
    'captcha',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_jslint',
    'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_sloccount'
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ShoesInvasion.urls'

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
                #'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ShoesInvasion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
# F up gitignore not working
# Asif : asif1234
# Ken : admin
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ShoesInvasion',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
        'min_length': 12,
    }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher', #Don't know if it is needed
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

RECAPTCHA_PUBLIC_KEY = '6Lcax7QiAAAAAFNjhILY9I7YKyTiIeU0u0FAq96M'
RECAPTCHA_PRIVATE_KEY = '6Lcax7QiAAAAAPDiSYSHISAGMqiMW6E01YsrtwDQ'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies" 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#EMAIL Backend
DEFAULT_FROM_EMAIL="marisschool@outlook.com"
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST="smtp.office365.com"
EMAIL_FROM = 'marisschool@outlook.com'
EMAIL_HOST_USER = 'marisschool@outlook.com'
EMAIL_HOST_PASSWORD='tcinrclkincpzois'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
PASSWORD_RESET_TIMEOUT = 14400

LOGGING = {
    'version':1,
    'loggers':{
        'user':{
            'handlers':['file'],
            'level':'INFO'
        },
        'inputvalidation':{
            'handlers':['file'],
            'level':'INFO'

        }
    },
    'handlers':{
        'file':{
            'level':'INFO',
            'class':'logging.FileHandler',
            'filename':f"logs/debug.log",
            'mode':'a',
            'encoding':'utf-8',
            'formatter':'verbose'
        }
    },
    'formatters':{
        'verbose':{
            'format':'{levelname} {message} {asctime:s}',
            'style':'{',
        },
    }
}
# Rules set for pages across application. 
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_HTTPONLY = True
# More Difficult to hijack user session. 
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_HTTPONLY = True
# Preventing Clickjacking
X_FRAME_OPTIONS = 'SAMEORIGIN'
# Serve Pages with 'x-content-type-options: nosniff' header. Prevents the browser from trying to mime-sniff the content-type of a response
SECURE_CONTENT_TYPE_NOSNIFF = True
# Instructs the browser to send a full URL, but only for same-origin links. No referrer will be sent for cross-origin links.
SECURE_REFERRER_POLICY = 'same-origin'
# Defense-in-depth protection against cross-origin attacks, especially those like Spectre 
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin'