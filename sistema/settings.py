# -*- coding: utf-8 -*-
"""
Django settings for sistema project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))
import urlparse
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
    ('Jose Sabastizagal','jsabastizagal@42.com.pe'),

    )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u4r60fyewf$p+#)c9_y%76xl9c3#5pr6#6)euk-gh85l9-gljn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.sites',
    'std',
    'bootstrapform',
  #  'south'
)

MIDDLEWARE_CLASSES = (
     'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'djangologging.middleware.LoggingMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'sistema.urls'

WSGI_APPLICATION = 'sistema.wsgi.application'

MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'upload')

MEDIA_URL ='/media/'



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'dbSTD',
        'USER': 'jose',
        'PASSWORD': 'jo71006',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

SITE_ID = 1

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
   '/home/jose/apps/tramite/std/static',
    #os.path.join(RUTA_PROYECTO,'static'),
)


STATIC_URL = '/static/'

STATIC_ROOT = 'static'

#STATIC_URL = os.path.join(RUTA_PROYECTO,'/static/')


ADMIN_MEDIA_PREFIX = '/home/jose/apps/tramite/std/static/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    )

TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO,'template'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    "django.core.context_processors.tz",
    'django.core.context_processors.i18n',
    'django.contrib.messages.context_processors.messages',
    #'grappelli.context_processors.admin_template_path',
  
)
