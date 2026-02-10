from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Dish, Category

def home(request):
    popular = Dish.objects.filter(is_popular=True, is_available=True)[:6]
    new = Dish.objects.filter(is_available=True).order_by('-created_at')[:6]
    return render(request, 'home.html', {'popular': popular, 'new': new})

def menu_list(request):
    q = request.GET.get('q', '')
    category = request.GET.get('cat', '')
    dishes = Dish.objects.all()

    if category:
        dishes = dishes.filter(category__slug=category)

    if q:
        dishes = dishes.filter(Q(name__icontains=q) | Q(description__icontains=q))

    categories = Category.objects.all()
    return render(request, 'menu/list.html', {'dishes': dishes, 'categories': categories, 'q': q, 'category': category})

def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'menu/detail.html', {'dish': dish})