from django.contrib import admin
from django.db import models
from .models import Setting , Theme_use , Help_questions,Team , Faq


# Register your models here.
class Help_questionsAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'create_at']

admin.site.register(Setting )
admin.site.register(Help_questions , Help_questionsAdmin)
admin.site.register(Theme_use )
admin.site.register(Team)
admin.site.register(Faq)