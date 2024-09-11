
from django.shortcuts import render
from menu.models import Menu

# Create your views here.


def home_view(request):
    # Получаем все меню
    menus = Menu.objects.all().prefetch_related('items')
    context = {
        'menus': menus
    }
    return render(request, 'menu/home.html', context)