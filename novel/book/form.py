#coding:utf-8
from django.core.exceptions import ValidationError
from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    name = forms.CharField(max_length='20', label=u'modif by form')

    def clean_name(self):
        raise ValidationError(u'哈哈，错了吧')

    class Meta:
        model = Book
