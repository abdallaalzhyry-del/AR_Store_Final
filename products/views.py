from django.shortcuts import render
from .models import Product

def product_list(request):
    # بنجيب القسم اللي الزبون اختاره من اللينك
    category_name = request.GET.get('category')
    
    if category_name:
        # لو اختار قسم معين
        products = Product.objects.filter(category=category_name)
    else:
        # لو لسه فاتح الموقع، نعرض كل حاجة
        products = Product.objects.all()
        
    # ركز في السطر اللي تحت ده، هو ده سر الحل:
    return render(request, 'products/index.html', {'items': products})