from django.shortcuts import render
from .models import Product

def product_list(request):
    # بنشوف الزبون داس على أنهي قسم (لو مفيش، بيبقى None)
    category_name = request.GET.get('category')
    
    if category_name:
        # لو اختار قسم، هات منتجات القسم ده بس
        products = Product.objects.filter(category=category_name)
    else:
        # ده اللي هيظهر أول ما يفتح الموقع (التيشرتات)
        products = Product.objects.filter(category='tshirt')
        
    return render(request, 'products/product_list.html', {'products': products})