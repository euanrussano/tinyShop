from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Category, Product

from cart.forms import CartAddProductForm

# Create your views here.
def index(request):
    return render(request, 'shop/index.html', {})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product/list.html',
                            {'category': category,
                             'categories': categories,
                             'products': products
                            })

def product_detail(request, category_slug=None, product_slug=None):
    product = get_object_or_404(Product, slug = product_slug, available=True)
    
    cart_product_form = CartAddProductForm()

    return render(request, 'shop/product/detail.html',
                            {'product': product,
                            'cart_product_form':cart_product_form})
