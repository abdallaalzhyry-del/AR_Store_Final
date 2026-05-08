from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]

# السطور اللي تحت دي هي اللي بتخلي الصور تظهر في المتصفح
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# كود إنشاء مستخدم مدير جديد تلقائياً ببيانات بسيطة
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@test.com', 'admin1234')
        print("Admin user created successfully!")
except Exception as e:
    print(f"Error creating admin: {e}")