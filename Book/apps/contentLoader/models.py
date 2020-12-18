from django.db import models
from datetime import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    """Категории"""
    category_name = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Book(models.Model):
    """Книги"""
    book_name = models.CharField('Название', max_length = 200)
    book_desc = models.TextField('Описание')
    book_img = models.TextField('Ссылка на изображение')
    book_author = models.CharField('Автор', max_length = 100)
    book_price = models.IntegerField('Цена')
    book_count = models.IntegerField('Количество')
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Comments(models.Model):
    date_create = models.DateTimeField('Дата создания комментарий')
    content = models.TextField('Содержание комментария')
    creator_user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket')
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(
        verbose_name='время', auto_now_add=True)
