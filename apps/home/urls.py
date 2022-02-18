from django.urls import path
from .views import Home , aboutus , search,contactus , terms_of_use , faq

urlpatterns = [
    path('' , Home , name='home'),
    path('about/' ,aboutus , name='about' ),
    path('search/' , search , name='search'),
    path('contact/' , contactus , name='contact'),
    path('terms_of_use/' , terms_of_use , name='terms_of_use'),
    path('faq/' , faq , name='faq')
]