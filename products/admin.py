from django.contrib import admin
from .models import Product, ProductImage
from django.utils.html import format_html
from django.urls import reverse

# تخصيص عناوين لوحة التحكم
admin.site.site_header = "A&R Fashion Control Panel"
admin.site.site_title = "A&R Admin"
admin.site.index_title = "إدارة منتجات البراند"

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 # قللتها لـ 1 عشان الزحمة، وممكن تضيف أكتر يدوي
    verbose_name = "صورة في المعرض"
    verbose_name_plural = "صور المعرض الإضافية"

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    
    # ترتيب الخانات في الجدول (الصورة أول حاجة عشان الشكل)
    list_display = ('display_image', 'name', 'category', 'price', 'status_badge', 'delete_button')
    
    # الخانات اللي تقدر تعدلها من بره (التصنيف والسعر والحالة)
    list_editable = ('category', 'price') 
    
    # الفلتر الجانبي (هو ده اللي هينظم لك "تيشرت" أو "بنطلون" في ثانية)
    list_filter = ('category', 'status')
    
    # البحث باسم المنتج
    search_fields = ('name',)
    
    # عدد المنتجات في الصفحة الواحدة (عشان الزحمة)
    list_per_page = 20

    # 1. شريط الحالة بشكل احترافي
    def status_badge(self, obj):
        colors = {
            'available': '#27ae60',    # أخضر
            'out_of_stock': '#e74c3c', # أحمر
            'last_piece': '#f39c12'    # برتقالي
        }
        return format_html(
            '<span style="background: {}; color: white; padding: 5px 12px; border-radius: 20px; '
            'font-weight: bold; font-size: 11px; display: inline-block; min-width: 80px; text-align: center;">{}</span>',
            colors.get(obj.status, '#333'),
            obj.get_status_display()
        )
    status_badge.short_description = 'حالة المخزون'

    # 2. زرار الحذف السريع بنمط أيقونة
    def delete_button(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name
        delete_url = reverse(f'admin:{app_label}_{model_name}_delete', args=[obj.pk])
        return format_html(
            '<a href="{}" style="background: #ff4d4d; color: white; padding: 4px 8px; '
            'border-radius: 5px; text-decoration: none; font-size: 14px;" title="حذف سريع">حذف 🗑️</a>',
            delete_url
        )
    delete_button.short_description = 'الإجراءات'

    # 3. عرض الصورة المصغرة بشكل دائري أو مربع أنيق (تم إصلاح السطر المقطوع وقفل الأقواس)
    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 55px; height: 55px; border-radius: 10px; '
                'border: 1px solid #ddd; object-fit: cover;" />',
                obj.image.url
            )
        return "لا توجد صورة"
    display_image.short_description = 'الصورة'

# تسجيل الموديل في الأدمن (تأكد إن السطر ده موجود في الآخر عشان يشتغل)
admin.site.register(Product, ProductAdmin)