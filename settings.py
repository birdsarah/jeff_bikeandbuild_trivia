import os
import logging
import private_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = private_settings.DEBUG

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['jeff.bonvaya.com']

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': private_settings.DATABASE_NAME,
        'USER': private_settings.DATABASE_USER,
        'PASSWORD': private_settings.DATABASE_PASSWORD,
        'HOST': private_settings.DATABASE_HOST,
        'PORT': '',
    }
}

SECRET_KEY = private_settings.SECRET_KEY

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Tools
    'south',

    # Apps
    'trivia',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/media/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public/media/static')

MEDIA_URL = '/media/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media/uploads')

# Additional places to find static
STATICFILES_DIRS = (
    'static',
)

# Additional places to find template:
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "bikeandbuild/templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    # Custom
    'trivia.context_processors.debug',
)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# configure logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
    filename = os.path.join(BASE_DIR, 'logs/app.log'),
    filemode = 'a'
)
