from django.db import models

from category.models import Category
from account.models import *



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey('main.Company', on_delete=models.CASCADE)
    author = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    text = models.TextField()
    info = models.CharField(max_length=300)
    price = models.PositiveIntegerField(default=0, help_text='Show in dollars')
    url = models.SlugField(max_length=200, unique=True)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'