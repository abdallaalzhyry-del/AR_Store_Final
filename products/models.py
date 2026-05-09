from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('available', 'متوفر'),
        ('out_of_stock', 'نفذت الكمية'),
        ('last_piece', 'أخر قطعة'),
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # التعديل هنا: جعلنا الصورة اختيارية لتجنب خطأ Read-only file system على Vercel
    image = models.ImageField(upload_to='product_images/', null=True, blank=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name

# الموديل لصور المعرض (Gallery) مع جعل الصور اختيارية أيضاً
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    # التعديل هنا: جعلنا الصور الإضافية اختيارية
    image = models.ImageField(upload_to='product_gallery/', verbose_name="صورة إضافية", null=True, blank=True)

    def __str__(self):
        return f"صورة لمنتج {self.product.name}"