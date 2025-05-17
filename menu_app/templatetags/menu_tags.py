from django import template
from ..models import MenuItem

register = template.Library()


def get_ancestors(item):
    """Возвращает список предков пункта, включая сам пункт."""
    ancestors = []
    while item:
        ancestors.append(item)
        item = item.parent
    return ancestors


def build_menu_tree_with_flags(items, ancestors, active_item):
    """Строит дерево меню с флагами активности и развернутости."""
    tree = {}
    for item in items:
        is_active = item == active_item
        # Узел развернут, если он в предках или является активным
        is_expanded = item in ancestors
        tree[item.id] = {
            'item': item,
            'is_active': is_active,
            'is_expanded': is_expanded,
            'children': []
        }
    for item in items:
        if item.parent_id:
            tree[item.parent_id]['children'].append(tree[item.id])
    return [tree[item.id] for item in items if item.parent_id is None]


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """Отрисовывает меню по заданному названию."""
    request = context['request']
    current_path = request.path
    # Один запрос к БД
    items = MenuItem.objects.filter(name=menu_name).order_by('order')
    # Определяем активный пункт
    active_item = None
    for item in items:
        if item.get_url() == current_path:
            active_item = item
            break
    # Получаем предков активного пункта
    ancestors = get_ancestors(active_item) if active_item else []
    # Строим дерево
    menu_tree = build_menu_tree_with_flags(items, ancestors, active_item)
    return {'menu_tree': menu_tree}
