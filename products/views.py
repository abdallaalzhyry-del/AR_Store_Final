from django.shortcuts import render
from .models import Product

def home(request):
    clothing_items = Product.objects.all() 
    # جرب نكتب اسم الملف علطول من غير كلمة products/
    return render(request, 'index.html', {'items': clothing_items})