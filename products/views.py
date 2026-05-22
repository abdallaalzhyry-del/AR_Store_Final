from django.shortcuts import render
from .models import Product

def product_list(request):
    # بنشوف الزبون داس على أنهي قسم (لو مفيش، بيبقى None)
    category_name = request.GET.get('category')
    
    if category_name:
        # لو اختار قسم، هات منتجات القسم ده بس
        products = Product.objects.filter(category=category_name)
    else:
        # لو فاتح الصفحة الرئيسية لأول مرة، نعرض كل المنتجات
        # أو ممكن تخليها تعرض قسم معين زي 'tshirt' فقط
        products = Product.objects.all()
        
    # التعديل هنا: اسم الملف index.html والمتغير اسمه items
    return render(request, 'products/index.html', {'items': products})