from django.shortcuts import render
from Product.models import Product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context_data = {
            'products': products
        }

        return render(request, 'products/products.html', context=context_data)
