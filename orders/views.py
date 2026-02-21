from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from menu.models import Dish
from .forms import CheckoutForm
from .models import Order, OrderItem


def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        messages.info(request, "Кошик порожній.")
        return redirect("cart:cart_detail")

    items_preview = []
    total = 0

    for dish_id, qty in cart.items():
        dish = get_object_or_404(Dish, id=dish_id)
        line_total = dish.price * qty
        total += line_total
        items_preview.append({"dish": dish, "qty": qty, "line_total": line_total})

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)

            if request.user.is_authenticated:
                order.user = request.user

            order.save()

            # 🔥 ОСЬ ГОЛОВНЕ — ПЕРЕНОСИМО СТРАВИ
            for dish_id, qty in cart.items():
                dish = Dish.objects.get(id=dish_id)

                OrderItem.objects.create(
                    order=order,
                    dish=dish,
                    quantity=qty,
                    price=dish.price
                )

            # 🔥 І ЛИШЕ ТЕПЕР ЧИСТИМО КОШИК
            request.session["cart"] = {}
            request.session.modified = True

            return redirect("orders:success", order_id=order.id)

    else:
        initial = {}
        if request.user.is_authenticated:
            initial["full_name"] = request.user.get_full_name() or request.user.username

        form = CheckoutForm(initial=initial)

    return render(request, "orders/checkout.html", {
        "form": form,
        "items": items_preview,
        "total": total,
    })


def success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/success.html", {"order": order})