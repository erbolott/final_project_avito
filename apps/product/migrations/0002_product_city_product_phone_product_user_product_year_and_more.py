# Generated by Django 4.0 on 2022-01-20 15:57

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(max_length=200, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='product',
            name='phone',
            field=models.CharField(max_length=20, null=True, verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.CharField(max_length=20, null=True, verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='category',
            name='keywords',
            field=models.CharField(max_length=255, null=True, verbose_name='ключевые слова'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=20, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='название категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='upload_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='время изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='время создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='image_product', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='product',
            name='keywords',
            field=models.CharField(max_length=255, null=True, verbose_name='ключевые словa'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=True, max_length=20, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='upload_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='время изменения'),
        ),
    ]