from django.shortcuts import render
  
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage




# Create your views here.

def index(request):
    return render(request,"home.html")