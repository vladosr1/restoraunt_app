from django.conf import settings
from django.db import models


class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_CONFIRMED = "confirmed"
    STATUS_COOKING = "cooking"
    STATUS_DELIVERING = "delivering"
    STATUS_DONE = "done"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = [
        (STATUS_NEW, "New"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_COOKING, "Cooking"),
        (STATUS_DELIVERING, "Delivering"),
        (STATUS_DONE, "Done"),
        (STATUS_CANCELED, "Canceled"),
    ]

    PAY_ONLINE = "online"
    PAY_CASH = "cash"
    PAYMENT_CHOICES = [
        (PAY_ONLINE, "Online"),
        (PAY_CASH, "Cash on delivery"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="orders",
    )

    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    comment = models.TextField(blank=True)

    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default=PAY_CASH)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    dish = models.ForeignKey("menu.Dish", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # ціна на момент покупки

    def __str__(self):
        return f"{self.dish} x{self.quantity}"