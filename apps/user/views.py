from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from apps.home.models import Setting
from apps.product.models import Category, Product
from .models import UserProfile
from apps.user.forms import SignUpForm , UpdateProfileForm , UpdateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return HttpResponse('Hello')


def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/profile')
        else:
            messages.warning(request, 'Ошибка входа! Логин или пароль неверны')
            return HttpResponseRedirect('/login')

    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'settings': settings,
        'category': category,
        'username': request.user.username,
    }
    return render(request, 'login_form.html', context)




def signup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # create data in profile table for user
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'users/user.jpg'
            data.save()
            messages.success(request, 'Успешно')
            return HttpResponseRedirect('/profile')
        else:
            messages.warning(request, 'Ошибка регистрации! пароль должен совпадать и состоять из 8 символов')
            return HttpResponseRedirect('/register')
    
    form = SignUpForm()
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'settings': settings,
        'category': category,
        'form': form,
    }
    return render(request, 'signup_form.html', context)


@login_required(login_url='/login')
def dashboard(request):
    settings = Setting.objects.get(pk=1)
    userProfile = UserProfile.objects.filter(user = request.user)
    context = {
        'settings' : settings,
        'userProfile' : userProfile
    }
    return render(request , 'dashboard.html' , context)



def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/login')
def settings_profile(request):
    settings = Setting.objects.get(pk=1)
    userProfile = UserProfile.objects.filter(user = request.user)
    context = {
        'settings' : settings,
        'userProfile' : userProfile
    }
    return render(request , 'settings_profile.html' , context)



@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return HttpResponseRedirect('/')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }

    return render(request, 'settings_profile.html',context)



# def update(request, id):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         # file = request.FILES.get('file')
#         post_update = UserProfile.objects.get(id=id)
#         post_update.title = title
#         post_update.description = description
#         # post_update.image = file
#         post_update.save()
#         return HttpResponseRedirect('/')
#     return render(request, 'posts/update.html')