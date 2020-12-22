  
from django.urls import path,include
from django.contrib import admin
from store import views

app_name = "store"

urlpatterns = [
    
    path('', views.index, name='home'),

   
    
]
