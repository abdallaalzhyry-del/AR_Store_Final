import os
import dj_database_url
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: حافظ على السرية عند الرفع الحقيقي
SECRET_KEY = 'django-insecure-cge%dwj5pup@ut80$^=ojx4vff(fg$k=xj(rta$-4mhx!1(1ij'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'cloudinary_storage', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary', 
    'products', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_shop.urls'

# --- تعديل الـ TEMPLATES لحل مشكلة TemplateDoesNotExist نهائياً ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'products', 'templates'),
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

WSGI_APPLICATION = 'my_shop.wsgi.application'

# --- ربط قاعدة بيانات Neon Postgres ---
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_5voDQSRq2PkU@ep-twilight-mode-aprd3dcq.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require',
        conn_max_age=600,
        ssl_require=True
    )
}

# Password validation
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
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Africa/Cairo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Cloudinary Storage settings
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dkdlnqlpr',
    'API_KEY': '482276949318357',
    'API_SECRET': 'nbeO_gSNDp1hNsh4BvW91pYtK98'
}

# تفعيل إعدادات الـ Config الإجبارية لمنع الإيرور على Vercel
cloudinary.config(
    cloud_name = CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key = CLOUDINARY_STORAGE['API_KEY'],
    api_secret = CLOUDINARY_STORAGE['API_SECRET'],
    secure = True
)

# النظام الجديد لإدارة الملفات المرفوعة والـ Static المتوافق مع Django 6+
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'