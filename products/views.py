from django.shortcuts import render
from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotInteger

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page=1):
    context = {
        'title': 'GeekShop - Catalog',
        'categories': ProductCategory.objects.all(),
    }
    products = ProductCategory.objects.filter(category_id=category_id) if category_id else ProductCategory.objects.all()

    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)