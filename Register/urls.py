from django.forms.forms import Form
from django.urls import path
from .views import index, register, register_hospital, register_tutor
from django.forms import forms

urlpatterns = [
    path('', index, name='index'),
    path('registro/', register, name='register'),
    path('registro_h/', register_hospital, name='register_h'),
    path('registro_t/', register_tutor, name='register_t'),
]