from email.mime import image
from django.shortcuts import render
from .models import Category, Product
from apps.home.models import Setting
from .forms import Add_listingForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from apps.user.models import UserProfile



# Create your views here.

def category_product(request,id , slug):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    catdata = Category.objects.get(pk = id)
    product = Product.objects.filter(category_id = id)

    context = {
        'settings' : settings,
        'category' : category,
        'product' : product,
        'catdata' : catdata,
    }
    return render(request , 'category_products.html' , context)


def product_detail(request,id , slug):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product = Product.objects.get(pk = id)
    catdata = Category.objects.get(product=id)
    userProfile = UserProfile.objects.get(pk=2)
 
    context = {
        'settings' : settings,
        'category' : category,
        'product' : product,
        'catdata' : catdata, 
        'username': request.user.username,
        'userProfile':userProfile
    } 
    return render(request , 'product_detail.html' , context)




def add_listing(request):
    if request.method == 'POST':
        form = Add_listingForm(request.POST , request.FILES)
        if form.is_valid():
            data = Product()
            data.title = form.cleaned_data['title']
            data.category = form.cleaned_data['category']
            data.image = form.cleaned_data['image']
            data.price = form.cleaned_data['price']
            data.description = form.cleaned_data['description']
            data.phone = form.cleaned_data['phone']
            data.city = form.cleaned_data['city']
            data.year = form.cleaned_data['year']

            data.user = request.user
            data.save()
            messages.success(request, 'Успешно')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Форма была неверной')
            return HttpResponseRedirect('/addlisting')
        

    form = Add_listingForm()
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'settings': settings,
        'category': category,
        'form': form,
    }
    return render(request , 'add_listing.html' , context)

