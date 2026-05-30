import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# تأكد من اسم المشروع بتاعك (my_shop)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shop.settings')

# تعريف الـ application الأساسي
application = get_wsgi_application()

# إضافة دعم WhiteNoise لملفات الـ Static
application = WhiteNoise(application)

# تعريف متغير 'app' لبيئة Vercel (مهم جداً لتجنب إيرور 500)
app = application