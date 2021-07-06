
from enum import auto
from django.db import models
from django.conf import settings


class Tag(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='слаг')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название')
    slug = models.SlugField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовки')
    content = models.TextField(max_length='Контент')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категрия')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    slug = models.SlugField(verbose_name='Слаг')
    views = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self. title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
