from django import template
from menu.models import Menu, MenuItem

register = template.Library()


@register.simple_tag(name='draw_menu')
def draw_menu(menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        items = MenuItem.objects.filter(menu=menu).order_by('order')
        return {'menu_items': items}
    except Menu.DoesNotExist:
        return {'menu_items': []}


def build_menu_tree(items):
    """ Построение дерева из плоского списка меню-элементов """
    menu_dict = {}
    for item in items:
        menu_dict[item.id] = {
            'id': item.id,
            'name': item.name,
            'url': item.url,
            'children': [],
            'parent_id': item.parent_id
        }

    # Добавляем детей
    for item in items:
        parent_id = item.parent_id
        if parent_id:
            menu_dict[parent_id]['children'].append(menu_dict[item.id])

    # Возвращаем корневые элементы
    return [item for item in menu_dict.values() if item['parent_id'] is None]