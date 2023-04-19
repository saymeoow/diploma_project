from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from onlinestore.models import Sneakers
from .cart import Cart
from .forms import CartAddSneakersForm


@require_POST
def cart_add(request, sneakers_id):
    cart = Cart(request)
    sneakers = get_object_or_404(Sneakers, id=sneakers_id)
    form = CartAddSneakersForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(sneakers=sneakers,
                 quantity=cd['quantity'],
                 sizes=cd['sizes'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, sneakers_id):
    cart = Cart(request)
    sneakers = get_object_or_404(Sneakers, id=sneakers_id)
    cart.remove(sneakers)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddSneakersForm(
            initial={'quantity': item['quantity'],
                     'sizes': item['sizes'],
                     'update': True})
    return render(request, 'cart.html', {'cart': cart})
