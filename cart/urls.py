from django.urls import path
from .views import cart_detail, add_to_cart
from . import views

app_name = 'cart'


urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<int:dish_id>/', views.add_to_cart, name='cart_increase'),
    path('decrease/<int:dish_id>/', views.cart_decrease, name='cart_decrease'),
]