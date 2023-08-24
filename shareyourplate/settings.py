"""
Django settings for shareyourplate project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary
import cloudinary_storage

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
# load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
WSGI_APPLICATION = 'shareyourplate.wsgi.app'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR.joinpath('static/')]
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'authentication',
    'recipes',
    'tailwind',
    'handler',
    'theme',
    'django_browser_reload',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

ROOT_URLCONF = 'shareyourplate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# model user

AUTH_USER_MODEL = 'authentication.User'

# Login url : redirect page if user try to access to a login_required page.

LOGIN_URL = 'login'

# redirect user after login/logout

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'login'

# Media paths

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR.joinpath('media/')

# Tailwind  
TAILWIND_APP_NAME = 'theme'

################# DEV

# DEBUG = True
# DJANGO_LOG_LEVEL='DEBUG'

# ALLOWED_HOSTS = ['127.0.0.1']
# INTERNAL_IPS = [ "127.0.0.1",]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {}

# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'console': {
#             'level':'DEBUG',
#             'class':'logging.StreamHandler',
#             'formatter': 'custom',
#         },
#     },
#     'loggers': {
#         'django':{
#             'handlers':['console'],
#             'level':'INFO'
#         }
#     },
#     'formatters': {
#         'custom': {
#             'format':  '{name} {asctime} {levelname} :: {message}',
#             'style': '{',
#         }
#     }
# }

#####################"" PROD

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static')

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': str(os.getenv('CLOUDINARY_CLOUD_NAME')),
#     'API_KEY': str(os.getenv('CLOUDINARY_API_KEY')),
#     'API_SECRET': str(os.getenv('CLOUDINARY_API_SECRET')),
# }

cloudinary.config(
    cloud_name = str(os.getenv('CLOUDINARY_CLOUD_NAME')),
    api_key = str(os.getenv('CLOUDINARY_API_KEY')),
    api_secret = str(os.getenv('CLOUDINARY_API_SECRET')),
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'URL': str(os.getenv('DATABASE_URL')),
        'NAME': str(os.getenv('PGNAME')),
        'USER': str(os.getenv('PGUSER')),
        'PASSWORD': str(os.getenv('PGPASSWORD')),
        'HOST': str(os.getenv('PGHOST')),
        'PORT': str(os.getenv('PGPORT')),
    }
}

# LOGGING = {
#     'version': 1,
#     'handlers': {
#         "file": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": BASE_DIR / "debug.log",
#         },
#     },
#     'loggers': {
#         'django':{
#             'handlers':['file'],
#             'level':'INFO'
#         }
#     },
#     'formatters': {
#         'custom': {
#             'format':  '{name} {asctime} {levelname} :: {message}',
#             'style': '{',
#         }
#     }
# }
