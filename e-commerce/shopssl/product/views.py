from django.shortcuts import render,get_object_or_404
from product.models import Category, Product

# Create your views here.



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'list.html', context)



def productdetail(request,slug):
    products=get_object_or_404(Product,slug=slug)

    return render(request,'productdetail.html',{'products':products})



def show_category(request,hierarchy=None):
    category_slug=hierarchy.split('/')
    category_queryset=list(Category.objects.all())
    all_slugs=[x.slug for x in category_queryset]
    parent=None
    for slug in category_slug:
        if slug in all_slugs:
            parent=get_object_or_404(Category,slug=slug)
        
        else:
            instance=get_object_or_404(Product,slug=slug)
            return render(request, "productdetail.html", {'instance':instance,})
    return render(request,"list.html",{'product_set':parent.product_set.all(),})