from django.shortcuts import render
from cart.cart import Cart
from orders.models import Order, OrderItem
from orders.forms import OrderCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
            )
            cart.clear()
            return render(request, "orders/order/success.html",
                          context={'order': order})
    else:
        user = request.user
        initial = {'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   'phone': user.profile.tel
                   }
        form = OrderCreationForm(initial=initial)
    return render(request, "orders/order/creates.html",
                  context={'form': form, 'cart': cart})


def cancel_order(request, order_id):
    pass
