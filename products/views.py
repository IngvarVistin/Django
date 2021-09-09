from django.shortcuts import render
from products.models import Product, ProductCategory

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)

def products(request, category_id=None):
    context = {
        'title': 'GeekShop - Catalog',
        'products': Product.objects.all(),
    }
    products = ProductCategory.objects.filter(category_id=category_id) if category_id else ProductCategory.objects.all()

    context['products'] = products
    return render(request, 'products/products.html', context)