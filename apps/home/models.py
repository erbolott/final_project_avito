from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100 , verbose_name='Название сайта' , null=True)
    logo = models.ImageField(upload_to='logo' , verbose_name='Логотип' , null=True)
    keywords = models.CharField(max_length=200 , verbose_name='Ключевые слова' , null=True)
    description = models.TextField(verbose_name='Описание сайта', null=True)

    # контакты 
    location = models.CharField(max_length=100 , verbose_name='Локация' , help_text='Мы находимся по адресу ул.Ленина 232', null=True, blank=True )
    phone = models.CharField(max_length=100 , verbose_name='Телефон' , blank=True , null=True)
    email = models.CharField(max_length=30 , verbose_name='email' , blank=True , null=True)

    # социальные сети
    facebook = models.CharField(max_length=200 , verbose_name='facebook' , blank=True , null=True)
    instagram = models.CharField(max_length=200 , verbose_name='instagram' , blank=True , null=True)
    twitter = models.CharField(max_length=200 , verbose_name='twitter' , blank=True , null=True)
    youtube = models.CharField(max_length=200 , verbose_name='youtube' , blank=True , null=True)

    about_page = RichTextUploadingField(null=True ,  blank=True )



    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Основные настройки'

    
# условия использования
class Theme_use(models.Model):

    theme_use = models.CharField(max_length=100 , verbose_name='Тема правил использования' ,null=True )
    description_use =models.TextField(verbose_name='Описание использования', null=True )
  

    def __str__(self):
        return self.theme_use

    class Meta:
        verbose_name_plural = 'Условия пользования'



# момент вопросов посититилей

class Help_questions(models.Model):
    name = models.CharField(max_length=40 , null=True , verbose_name='Имя')
    email = models.CharField(max_length=250 , null=True , verbose_name='email')
    subject = models.CharField(max_length=250 , null=True , verbose_name='Тема')
    text = models.TextField(null=True , verbose_name='Текст')
    create_at = models.DateTimeField(auto_now_add=True , null=True, verbose_name='Отправлено')

    def __str__(self):
        return f"{self.name} | {self.email}"


    class Meta:
        verbose_name = 'Вопросы от поситителей'
        verbose_name_plural = 'Вопросы от поситителей'


# команда авито
class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', null=True)
    image = models.ImageField(upload_to='team/' ,verbose_name='Фото' ,null=True)
    rank = models.CharField(max_length=100 , verbose_name='Звание в компании',null=True)
    instagram =models.CharField(max_length=100 , verbose_name='instagram',null=True , blank=True)

    def __str__(self):
        return f"{self.name} | {self.rank}"

    class Meta:
        verbose_name = 'Наша команда'
        verbose_name_plural = 'Наша команда'

    
# FAQ
class Faq(models.Model):
    question = models.CharField(max_length=200 ,null=True , verbose_name='Вопросы')
    answer = models.TextField(null=True, verbose_name='Ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural='Часто задаваемые вопросы'