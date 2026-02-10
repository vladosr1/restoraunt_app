from django.conf import settings
from django.db import models
from menu.models import Dish

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('online', 'Онлайн'),
        ('cash', 'Готівка при отриманні'),
    ]
    STATUS_CHOICES = [
        ('new', 'Нове'),
        ('confirmed', 'Підтверджене'),
        ('paid', 'Оплачене'),
        ('completed', 'Завершене'),
        ('cancelled', 'Скасоване'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.PROTECT)
    dish_name_snapshot = models.CharField(max_length=200)
    price_snapshot = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)