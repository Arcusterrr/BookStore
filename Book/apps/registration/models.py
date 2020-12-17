from django.db import models


class User(models.Model):
    user_name = models.CharField('Имя пользователя', max_length=200)
    user_login = models.CharField('Логин', max_length=200)
    password = models.TextField('Пароль')

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
