#coding:utf-8
from django.db import models

STATUS = {
    0: u'正常',
    1: u'审核',
    2: u'删除',
}


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')

    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'名称')
    alias = models.CharField(max_length=40, verbose_name=u'英文名')
    desc = models.CharField(max_length=100, blank=True, verbose_name=u'描述', help_text=u'点击分类之后显示')

    category = models.ForeignKey(Category, default=None, blank=True, null=True, verbose_name=u'分类')
    tags = models.CharField(max_length=100, blank=True, verbose_name=u'标签')

    status = models.IntegerField(default=0, choices=STATUS.items(), verbose_name=u'状态')

    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        return self.name

    class meta:
        app_label = u'图书'
