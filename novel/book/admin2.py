#coding:utf-8
from django.contrib import admin

import djadmin2

from .models import Book, Category


class BookAdmin(djadmin2.ModelAdmin):
    search_fields = ('name', 'alias')
    fields = ('name', 'alias', 'desc', 'category', 'tags', 'status',)
    list_display = ('name', 'category', 'create_time')

    list_per_page = 15
    save_on_top = True


class CategoryAdmin(djadmin2.ModelAdmin):
    list_display = ('name', 'create_time')
    list_per_page = 15


djadmin2.default.register(Book, BookAdmin)
djadmin2.default.register(Category, CategoryAdmin)
