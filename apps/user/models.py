from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE ,null=True)
    phone = models.CharField(max_length=25 ,null=True)
    address = models.CharField(max_length=255 ,null=True)
    city = models.CharField( max_length=255 ,null=True)
    country = models.CharField( max_length=255 ,null=True)
    image = models.ImageField(null=True, upload_to='users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ['+self.user.username+'] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="60px">'.format(self.image.url))
    image_tag.short_description = "Аватарка"

    class Meta:
        verbose_name_plural = 'Пользователи'