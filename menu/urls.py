from django.urls import path 
from .views import home, menu_list, dish_detail

urlpatterns = [
    path('', menu_list, name='menu_list'),
    path('<int:pk>/', dish_detail, name='dish_detail'),
]