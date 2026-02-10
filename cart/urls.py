from django.urls import path
from .views import cart_detail, add_to_cart

app_name = 'cart'


urlpatterns =[
    path('', cart_detail, name="cart_detail"),
    path("add/<int:dish_id>/", add_to_cart, name="add_to_cart"),
]