# -*- coding: utf-8 -*-
from django.db import models
from cloudinary.models import CloudinaryField 

class Product(models.Model):
    STATUS_CHOICES = [
        ('available', 'متوفر'),
        ('out_of_stock', 'نفذت الكمية'),
        ('last_piece', 'أخر قطعة'),
    ]
    
    CATEGORY_CHOICES = [
        ('tshirt', 'تيشرت'),
        ('pants', 'بنطلون'),
        ('shirt', 'قميص'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tshirt', verbose_name="القسم")
    
    # تم التعديل: شيلنا 'image' الأولى عشان نمنع تداخل الـ verbose_name
    image = CloudinaryField(null=True, blank=True, verbose_name="الصورة الأساسية") 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="حالة المنتج")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name="المنتج")
    
    # تم التعديل هنا أيضاً
    image = CloudinaryField(null=True, blank=True, verbose_name="صورة إضافية")

    class Meta:
        verbose_name = "صورة إضافية"
        verbose_name_plural = "معرض الصور الإضافية"

    def __str__(self):
        return f"صورة لمنتج {self.product.name}"