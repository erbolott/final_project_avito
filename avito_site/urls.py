from os import name
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from apps.product.views import category_product , product_detail ,add_listing 
from apps.user.views import login_form, signup_form , dashboard , logout_form ,settings_profile




urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('apps.home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/', include('apps.product.urls')),
    path('category/<int:id>/<slug:slug>', category_product , name='category_product'),
    path('product/<int:id>/<slug:slug>', product_detail , name='product_detail'),
    path('user/', include('apps.user.urls')),
    path('login/' , login_form , name='login'),
    path('register/' , signup_form , name='signup_form'),
    path('profile/' , dashboard , name='dashboard'),
    path('profile/addlisting/' , add_listing , name='add_listing'),
    path('logout/', logout_form, name='logout'),
    path('profile_settings/',settings_profile,name='settings_profile'),
    path('accounts/' , include('allauth.urls')) # неудачная попытка вход через социальные сети
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)