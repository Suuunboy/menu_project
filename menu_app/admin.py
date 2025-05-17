from django.contrib import admin

from django.contrib import admin
from menu_app.models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'url', 'parent', 'order')
    list_filter = ('name',)
    search_fields = ('title', 'url')
