from django.db import models

from category.models import Category
from account.models import *


class Image(models.Model):
    image = models.ImageField(upload_to='post_and_products_images/')
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Product(models.Model):
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey('main.Company', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    product_text = models.TextField()
    info = models.CharField(max_length=300)
    price = models.PositiveIntegerField(default=0, help_text='Show in dollars')
    product_url = models.SlugField(max_length=200, unique=True)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'