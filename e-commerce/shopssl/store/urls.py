  
from django.urls import path,include
from django.contrib import admin
from store import views

app_name = "store"

urlpatterns = [
    
    path('', views.index, name='home'),

    #path('ssl/', views.post, name='post'),
    #path('ssl/<path:hierarchy>/', views.show_category,name='category'),
    #path('<slug:slug>/', views.postdetail,name='postdetail'),
    
]
