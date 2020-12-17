# Generated by Django 3.1.3 on 2020-11-23 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200, verbose_name='Название')),
                ('book_desc', models.TextField(verbose_name='Описание')),
                ('book_img', models.TextField(verbose_name='Ссылка на изображение')),
                ('book_author', models.CharField(max_length=100, verbose_name='Автор')),
                ('book_price', models.IntegerField(verbose_name='Цена')),
                ('book_count', models.IntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
