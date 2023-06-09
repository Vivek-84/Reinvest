from django.contrib import admin
from django.urls import path,include
from App import views

urlpatterns = [
    
    path('', views.Index),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact, name=''),
    path('analytics/',views.analytics, name= ''),
    path('mlmodel/', views.mlmodel, name = '')
]   



