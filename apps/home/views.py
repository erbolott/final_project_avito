from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Setting , Theme_use ,Team , Faq
from apps.product.models import Category, Product
from apps.home.forms import SearchForm , Help_questionsForm
from django.contrib import messages
from apps.user.models import UserProfile


# Create your views here.

# главная страница
def Home(requets):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'settings' : settings,
        'category' : category
    }
    return render(requets , 'index.html' , context)



# страница о нас
def aboutus(requets):
    settings = Setting.objects.get(pk=1)
    team = Team.objects.all()
    posts_total = Product.objects.all().count()
    users_total = UserProfile.objects.all().count
    context = {
        'settings' : settings,
        'team' : team,
        'posts_total' :posts_total,
        'users_total' : users_total
    }
    return render(requets , 'aboutus.html' , context)


#страница котакты
def contactus(request):
    if request.method == 'POST':
        form = Help_questionsForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение отправлено')
        else:
            messages.warning(request, 'Форма была неверной')
            return HttpResponseRedirect('/contact')

    form = Help_questionsForm()
    settings = Setting.objects.get(pk=1)
    context = {
        'settings' : settings,
        'form' : form
    }
    return render(request , 'contactus.html' , context)



# страница словия исользование
def terms_of_use(requets):
    settings = Setting.objects.get(pk=1)
    terms_of_use = Theme_use.objects.all()
    context = {
        'settings' : settings,
        'terms_of_use' : terms_of_use
    }
    return render(requets , 'terms_of_use.html' , context)


# поисковая система 
def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                products=Product.objects.filter(title__icontains=query) 
            else:
                products = Product.objects.filter(title__icontains=query)
            
            category = Category.objects.all()
            settings = Setting.objects.get(pk=1)
            context = {
                'products':products,
                'query':query,
                'category':category,
                'settings':settings,
            }
            return render(request, 'search_products.html', context)
    return HttpResponseRedirect('/')



# faq 
def faq(request):
    settings = Setting.objects.get(pk=1)
    faq = Faq.objects.all()
    context = {
        'faq' : faq,
        'settings' :settings
    }
    return render(request , 'faq.html' , context)