from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('akk', views.akk, name='akk'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
]