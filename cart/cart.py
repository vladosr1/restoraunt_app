from decimal import Decimal
from menu.models import Dish

CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, dish_id, quantity=1, override=False):
        dish_id = str(dish_id)
        if dish_id not in self.cart:
            self.cart[dish_id] = {'qty': 0}
        if override:
            self.cart[dish_id]['qty'] = quantity
        else:
            self.cart[dish_id]['qty'] += quantity
        self.save()

    def remove(self, dish_id):
        dish_id = str(dish_id)
        if dish_id in self.cart:
            del self.cart[dish_id]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session[CART_SESSION_ID] = {}
        self.save()

    def __iter__(self):
        dish_ids = self.cart.keys()
        dishes = Dish.objects.filter(id__in=dish_ids)
        dish_map = {str(d.id): d for d in dishes}

        for dish_id, item in self.cart.items():
            dish = dish_map.get(dish_id)
            if not dish:
                continue
            qty = item['qty']
            price = dish.price
            yield {
                'dish': dish,
                'qty': qty,
                'price': price,
                'total': price * qty,
            }

    def total_price(self):
        total = Decimal('0.00')
        for it in self:
            total += it['total']
        return total