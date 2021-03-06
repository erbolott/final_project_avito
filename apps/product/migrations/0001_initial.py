# Generated by Django 4.0 on 2022-01-02 14:59

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='название категории')),
                ('keywords', models.CharField(max_length=255, verbose_name='ключевые слова')),
                ('image', models.ImageField(upload_to='category', verbose_name='фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('upload_at', models.DateTimeField(auto_now=True, verbose_name='время изменения')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=20, verbose_name='Статус')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
            options={
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название товара')),
                ('keywords', models.CharField(max_length=255, verbose_name='ключевые словa')),
                ('image', models.ImageField(upload_to='image_product', verbose_name='фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(null=True, unique=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('upload_at', models.DateTimeField(auto_now=True, verbose_name='время изменения')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=20, verbose_name='Статус')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='категория')),
            ],
            options={
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
