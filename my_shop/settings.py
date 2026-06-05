import os
import dj_database_url
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-cge%dwj5pup@ut80$^=ojx4vff(fg$k=xj(rta$-4mhx!1(1ij'
DEBUG = True
ALLOWED_HOSTS = ['.vercel.app', '127.0.0.1', 'localhost', '*']

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

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_5voDQSRq2PkU@ep-twilight-mode-aprd3dcq.c-7.us-east-1.aws.neon.tech/neondb?sslmode=require',
        conn_max_age=600,
        ssl_require=True
    )
}

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Africa/Cairo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []

MEDIA_URL = '/media/'
MEDIA_ROOT = '/tmp/media/'

# ✅ تم تحديث الـ API SECRET بالكود الجديد الحقيقي
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dkdlnqlpr',
    'API_KEY': '941419429723414',  
    'API_SECRET': 'UdV_KU7amXu4Cs9t7d6v4RUo1nA'
}

cloudinary.config(
    cloud_name = 'dkdlnqlpr',
    api_key = '941419429723414',     
    api_secret = 'UdV_KU7amXu4Cs9t7d6v4RUo1nA',
    secure = True
)

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage", 
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage", 
    },
}

WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_MIME_TYPES = {
    '.js': 'application/javascript', 
    '.css': 'text/css'
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'