from django.shortcuts import render, redirect, get_object_or_404
from menu.models import Dish

def cart_detail(request):
    cart = request.session.get('cart', {})
    dishes = Dish.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for dish in dishes:
        quantity = cart[str(dish.id)]
        item_total = dish.price * quantity
        total += item_total

        cart_items.append({
            'dish': dish,
            'quantity': quantity,
            'total': item_total
        })

    return render(request, 'cart/detail.html', {
        'cart_items': cart_items,
        'total': total
    })


def add_to_cart(request, dish_id):
    cart = request.session.get('cart')

    if cart is None:
        cart = {}

    dish_id = str(dish_id)

    cart[dish_id] = cart.get(dish_id, 0) + 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart:cart_detail')