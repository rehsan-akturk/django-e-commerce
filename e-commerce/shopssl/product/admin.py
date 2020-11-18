from django.contrib import admin

# Register your models here.

from product.models import Product,Category,Subcategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)



class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory_title', 'slug']

    class Meta:
        model = Subcategory


admin.site.register(Subcategory, SubCategoryAdmin)
