django-managed_menu
-----------

Managed via the administrative part, a tree-like menu.

Installation & Configuration:
-----------------------------

1. ``Download ZIP``

2. Add ``menu`` to your ``INSTALLED_APPS``

3. ``./manage.py migrate managed_menu`` 

4. Add a Menu (eg called ``managedmenu``) and add some items to that menu

5. In your template, load the menu tags and name your menu.

   .. code-block:: html+django

                {% load managedmenu %}
                <div>{% draw_menu you_name_menu %}</div>
Important:
----------
Urls of menu sections should be specified with delimiters (i.e. ``/about/``, ``/products/``, ``/home/``) 

Submenus:
---------
Linking the submenu to the parent menu is done using the parent field title and the child field parent_title
(i.e. parent.title = ``about``, children.parent_title = ``about``) 
