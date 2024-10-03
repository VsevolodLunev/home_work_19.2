# Generated by Django 5.1.1 on 2024-10-03 12:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('name', models.CharField(help_text='Название категории', max_length=100, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateField(verbose_name='Дата последнего изменения в базе данных')),
                ('created_at', models.DateField(verbose_name='Дата записи в базу данных')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание товара')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='catalog/photo', verbose_name='Фото товара')),
                ('price', models.IntegerField(help_text='Цена в рублях', verbose_name='Цена')),
                ('name', models.CharField(help_text='Выберите продукт', max_length=100, verbose_name='Название продукта')),
                ('category', models.ForeignKey(help_text='Введите название категории', max_length=100, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['category', 'price'],
            },
        ),
    ]
