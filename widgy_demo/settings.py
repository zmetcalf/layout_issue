"""
Django settings for widgy_demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%-zfnu++(b0upnucfv%&az$mda-oh-b+(^aa(z(ga*iwga*@n3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    'django.contrib.comments',
    'django.contrib.sites',
    'filebrowser_safe',
    'grappelli_safe',

    'widgy',
    'widgy.contrib.page_builder',
    'widgy.contrib.form_builder',
    'widgy.contrib.widgy_mezzanine',
    'widgy.contrib.urlconf_include',
    'widgy_blog',

    'django.contrib.admin',

    'filer',
    'easy_thumbnails',
    'compressor',
    'argonauts',
    'scss',
    'sorl.thumbnail',
    'south',

    'debug_toolbar',

    'widgets',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mezzanine.core.request.CurrentRequestMiddleware',
    'mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware',
    'mezzanine.pages.middleware.PageMiddleware',
    'widgy.contrib.urlconf_include.middleware.PatchUrlconfMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "mezzanine.conf.context_processors.settings",
    'mezzanine.pages.context_processors.page',
)

ROOT_URLCONF = 'widgy_demo.urls'

WSGI_APPLICATION = 'widgy_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '..', "static")

PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
TESTING = False
GRAPPELLI_INSTALLED = True
SITE_ID = 1

ADD_PAGE_ORDER = (
    'widgy_mezzanine.WidgyPage',
)

WIDGY_MEZZANINE_SITE = 'widgy_demo.site.site'

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

COMPRESS_ENABLED = True

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
)

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

ADMIN_MENU_ORDER = [
    ('Widgy', (
        'pages.Page',
        'page_builder.Callout',
        'form_builder.Form',
        ('Review queue', 'review_queue.ReviewedVersionCommit'),
    )),
]

URLCONF_INCLUDE_CHOICES = (
    ('blog.urls', 'Blog'),
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = (
    '127.0.0.1',
)
