from django.urls import path
from . import views

urlpatterns = [
    # غيرنا views.home لـ views.product_list عشان تطابق اسم الوظيفة اللي كتبناها
    path('', views.product_list, name='home'),
]