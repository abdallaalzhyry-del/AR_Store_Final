import os
import dj_database_url
from pathlib import Path

# المسار الرئيسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: حافظ على السرية عند الرفع الحقيقي
SECRET_KEY = 'django-insecure-cge%dwj5pup@ut80$^=ojx4vff(fg$k=xj(rta$-4mhx!1(1ij'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'cloudinary_storage', # التعديل: لازم يكون قبل staticfiles
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary', # التعديل: إضافة مكتبة السحاب
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
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'ar' 
TIME_ZONE = 'Africa/Cairo' 
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' 
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- التعديل: Media files باستخدام Cloudinary ---
# ده عشان يحل مشكلة الـ Read-only file system في Vercel
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dv9yv68sh', 
    'API_KEY': '742337775988225',
    'API_SECRET': '4U_X_IayC0Wn_1G29L8-oI2i2Fw'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Deployment trigger