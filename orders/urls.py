from django.urls import path
from .import views

app_name = "orders"

urlpatterns = [
    path("checkout/", views.checkout, name="checkout"),
    path("success/<int:order_id>/", views.success, name="success"),
    path("my/", views.my_orders, name="my_orders"),
    path("my/<int:order_id>", views.order_detail, name="order_detail"),
]