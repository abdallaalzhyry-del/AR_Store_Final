from django.db import models
from cloudinary.models import CloudinaryField 

class Product(models.Model):
    STATUS_CHOICES = [
        ('available', 'متوفر'),
        ('out_of_stock', 'نفذت الكمية'),
        ('last_piece', 'أخر قطعة'),
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # تعديل: حذفنا كلمة 'image' من البداية لتجنب تضارب التسمية
    image = CloudinaryField(null=True, blank=True, verbose_name="الصورة الأساسية") 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    # تعديل: صلحنا السطر اللي كان مطلع الأيرور الأحمر عندك
    image = CloudinaryField(null=True, blank=True, verbose_name="صورة إضافية")

    def __str__(self):
        return f"صورة لمنتج {self.product.name}"