from django.db import models

class Product(models.Model):
    STATUS_CHOICES = [
        ('available', 'متوفر'),
        ('out_of_stock', 'نفذت الكمية'),
        ('last_piece', 'أخر قطعة'),
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/') # الصورة الأساسية
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.name

# الموديل الجديد لصور المعرض (Gallery)
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_gallery/', verbose_name="صورة إضافية")

    def __str__(self):
        return f"صورة لمنتج {self.product.name}"