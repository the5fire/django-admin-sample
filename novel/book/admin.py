#coding:utf-8
from django.contrib import admin
from xadmin import site

from .models import Book, Category
from .form import BookForm

class BookBaseAdmin(object):
    search_fields = ('name', 'alias')
    fields = ('name', 'alias', 'desc', 'category', 'tags', 'status',)
    list_display = ('name', 'alias', 'category', 'create_time', 'preview')

    form = BookForm

    list_per_page = 15
    save_on_top = True


    def preview(self, obj):
        return u'<a href="%s/">编辑</a>' % obj.id
    preview.short_description = u'操作'
    preview.allow_tags = True


class BookAdmin(BookBaseAdmin, admin.ModelAdmin):
    pass


class CategoryBaseAdmin(object):
    list_display = ('name', 'create_time')
    list_per_page = 15


class CategoryAdmin(CategoryBaseAdmin, admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)

site.register(Book, BookBaseAdmin)
site.register(Category, CategoryBaseAdmin)
