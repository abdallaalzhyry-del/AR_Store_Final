from django.shortcuts import render
from .models import Product

def product_list(request):
    # بنجيب القسم اللي الزبون اختاره من اللينك
    category_name = request.GET.get('category')
    
    if category_name:
        # لو اختار قسم معين (تأكد إن الحروف متطابقة مع اللي في الموديل)
        products = Product.objects.filter(category=category_name)
    else:
        # لو لسه فاتح الموقع، نعرض كل حاجة
        products = Product.objects.all()
        
    # التعديل هنا: شيلنا كلمة 'products/' عشان يقرأ 'index.html' مباشرة 
    # من فولدر templates اللي إنت عرفته في الـ settings
    return render(request, 'index.html', {'items': products})