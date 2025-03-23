from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Category
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm

def product_list(request):
    """
    Вывод всего каталога
    """
    products = Product.objects.filter(available=True).order_by('name')
    return render(request, 'product/list.html', context={'products': products})



def product_detail(request, id, slug):
    """
    Вывод отдельного товара
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_add_product_form = CartAddProductForm()
    return render(request, 'product/detail.html',
                  context={'product': product,
                           'cart_add_product_form': cart_add_product_form})
