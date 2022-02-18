from apps.product.models import Product
from django.forms import ModelForm , TextInput , Textarea
from django.utils.safestring import mark_safe


class Add_listingForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title' , 'category' , 'price' , 'year' , 'description' ,'image','phone','city' ]

        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control',
            }),
            "price" : TextInput(attrs={
                'class' : 'form-control',
            }),

            "description" : Textarea(attrs={
                'class' : 'form-control',
            }),

            "year" : TextInput(attrs={
                'class' : 'form-control',
            }),
            "phone" : TextInput(attrs={
                'class' : 'form-control',
            }),
            "city" : TextInput(attrs={
                'class' : 'form-control',
            }),
        }

