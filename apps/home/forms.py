from django import forms
from django.forms import ModelForm , TextInput , Textarea
from .models import Help_questions

class SearchForm(forms.Form):
    query = forms.CharField(max_length=255)
    catid = forms.IntegerField()

class Help_questionsForm(ModelForm):
    class Meta:
        model = Help_questions
        fields = ['name' , 'email' , 'subject' , 'text' ,]

        widgets = {
            "name" : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' :'Имя'
            }),
            "email" : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' :'Телефон или электронная почта'
            }),

            "text" : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' :'Написать сообщение'
            }),

            "subject" : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' :'Тема'
            }),
        }
