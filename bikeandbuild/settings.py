import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if 'DEBUG' in os.environ:
    DEBUG = os.environ['DEBUG']
else:
    DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Sarah Bird', 'sarah@bonvaya.com'),
    ('Jeffrey Goodwin', 'jeffreyhgoodwin@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {}

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config()
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DATABASE_NAME'],
            'USER': os.environ['DATABASE_USER'],
            'PASSWORD': os.environ['DATABASE_PASSWORD'],
            'HOST': os.environ['DATABASE_HOST'],
            'PORT': '',
        }
    }

SECRET_KEY = os.environ['SECRET_KEY']

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
    'storages',
    'boto',

    # Apps
    'bikeandbuild',
    'trivia',
    'pages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bikeandbuild.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['immense-wildwood-2394.herokuapp.com',
                 'www.jhgoodwin.com']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/uploads')


# Additional places to find template:
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
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
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
}

if DEBUG is True:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    try:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'smtp.sendgrid.net'
        EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
        EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
        EMAIL_PORT = 587
        SERVER_EMAIL = 'jeffreyhgoodwin@gmail.com'
        EMAIL_USE_TLS = True
    except Exception as e:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Storage on S3 settings are stored as os.environs to keep settings.py clean
if DEBUG is False:
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
    MEDIA_URL = '%smedia/uploads/' % S3_URL
