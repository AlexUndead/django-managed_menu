from django import template
from django.core.cache import cache
from django.urls import path
from menu.models import Menu, MenuItem

register = template.Library()

def draw_menu(parser, token):
    try:
        tag_name, menu_name = token.split_contents()
    except:
        raise template.TemplateSyntaxError("Enter a menu name")
    return MenuObject(menu_name)


class MenuObject(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name
        self.has_active_item = False

    def get_raw_menu_items(self):
        menu_model_objects = Menu.objects.raw(
                    """SELECT *
                    FROM managed_menu_menuitem item
                    INNER JOIN managed_menu_menu menu
                    ON item.menu_id = menu.id
                    WHERE menu.name='{}'
                    ORDER BY item.order
                    """.format(self.menu_name))

        return [{'title':m.title, 'url':m.url, 'parent_title':m.parent_title, 'order':m.order, 'active':self.is_active_item(m.url)} for m in menu_model_objects]

    def collect_menu(self):
        if not self.raw_menu_items:
            return []

        collect_menu_items = []
        parent_items = [x for x in self.raw_menu_items if not x['parent_title']]
        items_without_parent = [x for x in self.raw_menu_items if x['parent_title']]

        for p_item in parent_items:
            p_item['child'] = self.collect_child_menu(items_without_parent, p_item['title'])
            collect_menu_items.append(p_item)

        return collect_menu_items

    def collect_child_menu(self, menu_items, parent_title):
        if not menu_items:
            return []

        child_menu_items = []

        for c_index in range(0, len(menu_items)):
            if menu_items[c_index]['parent_title'] == parent_title:
                menu_items[c_index]['child'] = self.collect_child_menu(menu_items, menu_items[c_index]['title'])
                child_menu_items.append(menu_items[c_index])

        return child_menu_items

    def is_active_item(self, item_url):
        if item_url == self.path:
            self.has_active_item = True
            return True
        else:
            return False


    def get_render_menu(self, menu_tree_items):
        render_menu = ''
        if not menu_tree_items:
            return render_menu

        render_menu += '<ul>'
        for menu_item in menu_tree_items:
            render_menu += '<li' + (' class="active"' if self.has_active_item else '') + '><a href="' + menu_item['url'] + '">' + menu_item['title'] + '</a></li>'

            if menu_item['active']:
                self.has_active_item = False

            if menu_item['child']:
                render_menu += self.get_render_menu(menu_item['child'])
        render_menu += '</ul>'

        return render_menu


    def render(self, context):
        self.path = context.request.get_full_path()
        self.raw_menu_items = self.get_raw_menu_items()

        return self.get_render_menu(self.collect_menu())


register.tag('draw_menu', draw_menu)
