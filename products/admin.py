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
    extra = 3
    verbose_name = "صورة في المعرض"
    verbose_name_plural = "صور المعرض الإضافية"

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    
    # ضيفنا 'category' هنا عشان تظهر في الجدول بره
    list_display = ('display_image', 'name', 'category', 'price', 'status', 'status_badge', 'delete_button')
    # ضيفنا 'category' هنا عشان تعدلها بسرعة من غير ما تدخل جوه المنتج
    list_editable = ('price', 'status', 'category') 
    # ضيفنا 'category' في الفلتر عشان تختار "البنطلونات" بس مثلاً
    list_filter = ('status', 'category')
    search_fields = ('name',)

    # 1. شريط الحالة
    def status_badge(self, obj):
        colors = {'available': '#27ae60', 'out_of_stock': '#e74c3c', 'last_piece': '#f39c12'}
        return format_html(
            '<span style="background: {}; color: white; padding: 5px 12px; border-radius: 15px; font-weight: bold; font-size: 11px;">{}</span>',
            colors.get(obj.status, '#333'),
            obj.get_status_display()
        )
    status_badge.short_description = 'شكل الحالة'

    # 2. زرار المسح السريع
    def delete_button(self, obj):
        app_label = obj._meta.app_label
        model_name = obj._meta.model_name
        delete_url = reverse(f'admin:{app_label}_{model_name}_delete', args=[obj.pk])
        return format_html(
            '<a href="{}" style="color: #e74c3c; font-size: 18px; text-decoration: none;" title="حذف">🗑️</a>',
            delete_url
        )
    delete_button.short_description = 'حذف سريع'

    # 3. عرض الصورة المصغرة
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 8px; object-fit: cover;" />', obj.image.url)
        return "No Image"
    display_image.short_description = 'الصورة'

# تسجيل الموديل
if admin.site.is_registered(Product):
    admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)