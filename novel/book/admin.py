#coding:utf-8
from django.contrib import admin

from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    search_fields = ('name', 'alias')
    fields = ('name', 'alias', 'desc', 'category', 'tags', 'status',)
    list_display = ('name', 'alias', 'category', 'create_time')

    list_per_page = 15
    save_on_top = True


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')
    list_per_page = 15


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
