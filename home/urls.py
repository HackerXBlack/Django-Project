from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("saveform", views.saveForm, name='saveform'),
    path('external_link/', views.external_link, name='external_link'),
    path('search', views.search, name='search'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login')
]