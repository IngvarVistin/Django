from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)

def products(request):
    context = {'title': 'GeekShop - Каталог',
               'products': [
                   {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
                   {'name': 'Синяя куртка The North Face', 'price': 23725},
                   {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
                   {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590},
                   {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890},
                        ]
               }
    return render(request, 'products/products.html', context)