from django.core.management.base import BaseCommand
from menu.models import Menu, MenuItem

class Command(BaseCommand):
    help = 'Создает объекты Menu и MenuItem'

    def handle(self, *args, **options):
        # Создание объекта меню
        menu = Menu.objects.create(name='Основное меню')

        # Создание объектов пунктов меню
        MenuItem.objects.create(
            name='Пункт 1',
            price=10.00,
            description='Описание 1',
            menu=menu,
            order=1
        )
        MenuItem.objects.create(
            name='Пункт 2',
            price=20.00,
            description='Описание 2',
            menu=menu,
            order=2
        )

        self.stdout.write(self.style.SUCCESS('Объекты созданы'))