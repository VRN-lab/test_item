from django import template
from django.utils.safestring import mark_safe
from menu.models import MenuItem

register = template.Library()


def render_menu_items(request, items, prefix):
    """
    Рекурсивно создаем меню и подменю
    """
    menu_html = '<ul>'
    for item in items:
        menu_html += f'<li><a href="{prefix}{item.url}?toggle={item.id}">{item.name}</a>'
        children = item.children.all()
        if children and str(item.id) in request.session.get('opened_menus', []):
            menu_html += render_menu_items(request, children, prefix)
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html


@register.simple_tag
def tree(request):
    """
    Создаем структура меню и подменю,
    которую можно вставить на любую страницу
    """
    prefix = request.scheme + '://' + request.get_host()
    root_items = MenuItem.objects.filter(parent__isnull=True)
    toggle_id = request.GET.get('toggle')
    if toggle_id:
        opened_menus = request.session.get('opened_menus', [])
        if toggle_id in opened_menus:
            opened_menus.remove(toggle_id)
        else:
            opened_menus.append(toggle_id)
        request.session['opened_menus'] = opened_menus

    return mark_safe(render_menu_items(request, root_items, prefix))
