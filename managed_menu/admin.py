from django.contrib import admin
from managed_menu.models import Menu, MenuItem

class MenuItemInline(admin.TabularInline):
    list_display = ['title', 'url', 'order', 'parent_name']
    model = MenuItem
    ordering = ('order',)

class MenuAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [MenuItemInline,]

admin.site.register(Menu, MenuAdmin)
