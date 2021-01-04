"""
Django settings for pyclist project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import warnings
import tempfile
from os import path, environ

from django.utils.translation import gettext_lazy as _
from django.core.paginator import UnorderedObjectListWarning

from pyclist import conf


# disable UnorderedObjectListWarning when using autocomplete_fields
warnings.filterwarnings('ignore', category=UnorderedObjectListWarning)


# Build paths inside the project like this: path.join(BASE_DIR, ...)
BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))

ADMINS = (
    ('Aleksey Ropan', 'aropan@clist.by'),
)

MANAGERS = ADMINS

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'noreply@clist.by'
EMAIL_HOST_PASSWORD = conf.EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SERVER_EMAIL = 'Clist <%s>' % EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = 'Clist <%s>' % EMAIL_HOST_USER

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['clist.by', 'dev.clist.by', 'localhost']

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = conf.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = 'DJANGO_RUNSERVER_DEBUG' in environ

# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'clist',
    'ranking',
    'tastypie',
    'my_oauth',
    'true_coders',
    'jsonify',  # https://pypi.python.org/pypi/django-jsonify/0.2.1
    'tastypie_swagger',
    'blog',
    'django_markdown',
    'tg',
    'notification',
    'crispy_forms',
    'events',
    'django_countries',
    'el_pagination',
    'django_static_fontawesome',
    'django_extensions',
    'django_user_agents',
    'django_json_widget',
    'django_ltree',
    'imagefit',
    'webpush',
    'django_postgres_reindex_command'
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'pyclist.middleware.RequestLoggerMiddleware',
)

if DEBUG:
    MIDDLEWARE += (
        'pyclist.middleware.DebugPermissionOnlyMiddleware',
        'django_cprofile_middleware.middleware.ProfilerMiddleware',
    )

ROOT_URLCONF = 'pyclist.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pyclist.context_processors.global_settings',
                'pyclist.context_processors.bootstrap_admin',
                'pyclist.context_processors.coder_time_info',
            ],
            'builtins': [
                'pyclist.templatetags.staticfiles',
                'clist.templatetags.extras',
                'imagefit.templatetags.imagefit',
                'django.contrib.humanize.templatetags.humanize',
            ],
        },
    },
]

WSGI_APPLICATION = 'pyclist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES_ = {
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': conf.DB_NAME,
        'USER': conf.DB_USER,
        'PASSWORD': conf.DB_PASSWORD,
        'HOST': conf.DB_HOST,
        'PORT': conf.DB_PORT,
    },
}

DATABASES = {
    'default': DATABASES_['postgresql'],
}
DATABASES.update(DATABASES_)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

USER_AGENTS_CACHE = 'default'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', _('English')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'nginx/static/')
STATIC_JSON_TIMEZONES = path.join(BASE_DIR, 'static', 'json', 'timezones.json')

STATICFILES_DIRS = [
    path.join(BASE_DIR, 'static'),
    path.join(BASE_DIR, 'third_party/x-editable/dist/bootstrap3-editable'),
    path.join(BASE_DIR, 'third_party/bootstrap/dist'),
    path.join(BASE_DIR, 'third_party/select2/dist'),
]

TASTYPIE_DEFAULT_FORMATS = ['json', 'jsonp', 'yaml', 'xml', 'plist']

LOGIN_URL = '/login/'

APPEND_SLASH = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'development': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': path.join(BASE_DIR, 'logs', 'dev.log'),
            'formatter': 'verbose',
        },
        'production': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'filename': path.join(BASE_DIR, 'logs', 'prod.log'),
            'formatter': 'verbose',
        },
        'telegrambot': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 7,
            'filename': path.join(BASE_DIR, 'logs', 'telegram.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
        'PIL': {
            'handlers': ['null'],
            'propagate': False,
        },
        'django': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
        },
        'telegrambot': {
            'handlers': ['telegrambot'],
            'level': 'DEBUG',
        },
        'django_super_deduper': {
            'handlers': ['console', 'development', 'production'],
            'level': 'ERROR',
        },
        '': {
            'handlers': ['console', 'development', 'production'],
            'level': 'DEBUG',
        },
    },
}


DATA_UPLOAD_MAX_NUMBER_FIELDS = 100000


TELEGRAM_TOKEN = conf.TELEGRAM_TOKEN
TELEGRAM_NAME = '@ClistBot'
TELEGRAM_ADMIN_CHAT_ID = conf.TELEGRAM_ADMIN_CHAT_ID

CRISPY_TEMPLATE_PACK = 'bootstrap3'

COUNTRIES_OVERRIDE = {
    'CZ': {'names': ['Czechia', 'Czech Republic', 'Чехия']},
    'MK': {'names': ['North Macedonia', 'Macedonia', 'Македония']},
    'PS': {'names': ['Palestine, State of', 'Palestine', 'Палестина']},
    'KR': {'names': ['South Korea', 'Republic of Korea', 'Южная Корея']},
    'MO': {'names': ['Macao', 'Macau', 'Макао']},
    'US': {'names': ['United States of America', 'United States', 'America', 'Virgin Islands', 'Соединенные Штаты Америки', 'США']},  # noqa
    'VN': {'names': ['Vietnam', 'Viet Nam', 'Вьетнам']},
    'GB': {'names': ['United Kingdom', 'United Kingdom of Great Britain', 'England', 'UK', 'Scotland', 'Northern Ireland', 'Wales', 'Великобритания', 'Англия', 'Шотландия']},  # noqa
    'MD': {'names': ['Moldova', 'Молдова', 'Молдавия']},
    'KG': {'names': ['Kyrgyzstan', 'Кыргызстан', 'Киргизия']},
    'RS': {'names': ['Serbia', 'Srbija', 'Сербия']},
    'HR': {'names': ['Croatia', 'Hrvatska', 'Хорватия']},
    'CN': {'names': ['China', '中国', 'Китай']},
    'PL': {'names': ['Poland', 'Republic of Poland', 'Польша']},
}

# DJANGO DEBUG TOOLBAR
if DEBUG:
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
    INTERNAL_IPS = ['dev.clist.by', 'localhost', '127.0.0.1', '::1']
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: (
            request.user.is_authenticated
            and request.user.has_perm('view_django_debug_toolbar')
            and ('debug_toolbar' in request.GET or '/__debug__' in request.path)
        ),
    }


# DJANGO CPROFILE
DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF = False

# DGANGO IMAGEFIT
IMAGEFIT_CACHE_ENABLED = True
IMAGEFIT_CACHE_BACKEND_NAME = 'django_imagefit'
CACHES[IMAGEFIT_CACHE_BACKEND_NAME] = {
    'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    'LOCATION': path.join(tempfile.gettempdir(), 'django_imagefit' + ('_debug' if DEBUG else ''))
}

# BOOSTRAP ADMIN
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

# WEBPUSH
WEBPUSH_SETTINGS = {
  'VAPID_PUBLIC_KEY': 'BLM8jbznhlOctmETpTmBhYCpS7YB9w57uopEKrUa44vPT8-ITGuruzxtfnV7K7tdYPUeoDGIokz7I2sboUqbwR8',
  'VAPID_PRIVATE_KEY': 'DuG3FnlFusaR1_2EXsdbezdVblJJTP4aIpB3DiwweFU',
  'VAPID_ADMIN_EMAIL': 'mailto:webmaster@clist.by',
}

# CONSTANTS
VIEWMODE_ = 'list'
OPEN_NEW_TAB_ = False
ADD_TO_CALENDAR_ = 'enable'
COUNT_PAST_ = 3
GROUP_LIST_ = True
HIDE_CONTEST_ = False
DEFAULT_TIME_ZONE_ = 'UTC'
HOST_ = 'dev.clist.by' if DEBUG else 'clist.by'
HTTP_HOST_ = 'http://' + HOST_
HTTPS_HOST_ = 'https://' + HOST_
EMAIL_PREFIX_SUBJECT_ = '[Clist] '
STOP_EMAIL_ = getattr(conf, 'STOP_EMAIL', False)
TIME_FORMAT_ = '%d.%m %a %H:%M'
LIMIT_N_TOKENS_VIEW = 3
LIMIT_TOKENS_VIEW_WAIT_IN_HOURS = 24
YES_ = ['', '1', 'yes', 'true']
ACE_CALENDARS_ = {
    'enable': {'id': 'enable', 'name': 'Enable'},
    'disable': {'id': 'disable', 'name': 'Disable'},
    'google': {'id': 1, 'name': 'Google'},
    'yahoo': {'id': 2, 'name': 'Yahoo'},
    'outlook': {'id': 3, 'name': 'Outlook'},
}
ORDERED_MEDALS_ = ['gold', 'silver', 'bronze']
THEMES_ = ['default', 'cerulean', 'cosmo', 'cyborg', 'darkly', 'flatly', 'journal', 'lumen', 'paper', 'readable',
           'sandstone', 'simplex', 'slate', 'spacelab', 'superhero', 'united', 'yeti']

CUSTOM_COUNTRIES_ = {
  'BY': ['BY', 'BPR'],
}

ISSUES_URL_ = 'https://github.com/aropan/clist/issues'
NEWS_URL_ = 'https://t.me/s/clistbynews'
DISCUSS_URL_ = 'https://t.me/clistbynews'
DONATE_URL_ = 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=47CJBL6B2XPM8&source=url'


class NOTIFICATION_CONF:
    EMAIL = 'email'
    TELEGRAM = 'telegram'
    WEBBROWSER = 'webbrowser'

    METHODS_CHOICES = (
        (EMAIL, 'Email'),
        (TELEGRAM, 'Telegram'),
        (WEBBROWSER, 'WebBrowser'),
    )


try:
    from .local_settings import *  # noqa
except ImportError:
    pass
