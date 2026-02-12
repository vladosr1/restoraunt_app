from django.urls import path
from .views import home, menu_list, dish_detail

urlpatterns = [
    path('', menu_list, name='menu_list'),  # всі страви
   path('category/<slug:slug>/', menu_list, name='menu_by_category'),  # категорія
    path('dish/<int:pk>/', dish_detail, name='dish_detail'),  # деталі страви
]