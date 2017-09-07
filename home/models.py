from django.db import models


class Category(models.Model):
    name = models.CharField('名称', max_length=16)


class Tag(models.Model):
    name = models.CharField('名称', max_length=16)


class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    content = models.TextField('正文')
    created = models.DateTimeField('发布时间', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
