from django.db import models
from django.contrib.auth.models import User
from menu.models import Dish


class CartItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.dish.name} ({self.quantity})"

    def total_price(self):
        return self.dish.price * self.quantity
