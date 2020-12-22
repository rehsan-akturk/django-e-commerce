from django.urls import path,include
from django.contrib import admin
from product import views

app_name = "product"


urlpatterns = [

    path('product/', views.product_list, name='product'),
    path('product/<path:hierarchy>/', views.show_category,name='category'),
    path('<slug:slug>/', views.productdetail,name='productdetail'),
    
    
]