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
    extra = 1 
    verbose_name = "صورة في المعرض"
    verbose_name_plural = "صور المعرض الإضافية"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    
    # هنا حطينا 'status' عشان تظهر كقائمة منسدلة
    list_display = ('display_image', 'name', 'category', 'price', 'status', 'status_badge', 'delete_button')
    
    # هنا شلنا أي اسم وهمي وحطينا الحقول الحقيقية فقط
    list_editable = ('category', 'price', 'status') 
    
    list_filter = ('category', 'status')
    search_fields = ('name',)
    list_per_page = 20

    # عرض الـ Badge الملونة
    def status_badge(self, obj):
        colors = {
            'available': '#27ae60', 
            'out_of_stock': '#e74c3c', 
            'last_piece': '#f39c12'
        }
        return format_html(
            '<span style="background: {}; color: white; padding: 5px 12px; border-radius: 20px; '
            'font-weight: bold; font-size: 11px; display: inline-block; min-width: 80px; text-align: center;">{}</span>',
            colors.get(obj.status, '#333'),
            obj.get_status_display()
        )
    status_badge.short_description = 'حالة المخزون (شكل)'

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

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 55px; height: 55px; border-radius: 10px; '
                'border: 1px solid #ddd; object-fit: cover;" />',
                obj.image.url
            )
        return "لا توجد صورة"
    display_image.short_description = 'الصورة'