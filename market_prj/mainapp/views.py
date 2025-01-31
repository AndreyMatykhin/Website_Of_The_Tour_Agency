from django.shortcuts import render, get_object_or_404

from .models import Product


# from django.template.defaultfilters import title


# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    title = 'Продукты'
    list_of_products = Product.objects.filter(is_active=True)
    content = {
        'title': title,
        'list_of_products': list_of_products,
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'Продукт'
    content = {
        'title': title,
        'product': get_object_or_404(Product, pk=pk)
    }
    return render(request, 'mainapp/product_details.html', content)
