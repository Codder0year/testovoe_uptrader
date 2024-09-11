from django.contrib import admin
from .models import Menu, MenuItem
# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'menu', 'order')
    list_filter = ('menu',)
    ordering = ('menu', 'order')