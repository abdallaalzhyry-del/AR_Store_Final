from django.db import models
from cloudinary.models import CloudinaryField 

class Product(models.Model):
    # خيارات الحالة (الموجودة عندك)
    STATUS_CHOICES = [
        ('available', 'متوفر'),
        ('out_of_stock', 'نفذت الكمية'),
        ('last_piece', 'أخر قطعة'),
    ]
    
    # خيارات الأقسام (اللي ضيفناها جديد)
    CATEGORY_CHOICES = [
        ('tshirt', 'تيشرت'),
        ('pants', 'بنطلون'),
        ('shirt', 'قميص'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    
    # حقل القسم الجديد
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='tshirt', 
        verbose_name="القسم"
    )
    
    image = CloudinaryField(null=True, blank=True, verbose_name="الصورة الأساسية") 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="حالة المنتج")

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField(null=True, blank=True, verbose_name="صورة إضافية")

    def __str__(self):
        return f"صورة لمنتج {self.product.name}"