from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    photo=models.ImageField(upload_to='products_category')
    date=models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    subcategory_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    subcategory_image = models.ImageField()
    subcategory_category = models.ForeignKey(
        Category, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.subcategory_title


class Product(models.Model):
    name=models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    photo = models.ImageField(upload_to='products')
    price=models.IntegerField()
    details=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_draft=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now=True)



    
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs) 

    
    


