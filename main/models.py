from urllib import request
from django.db import models


from post.models import *
from product.models import *
from category.models import *
from account.models import *


class Image(models.Model):
    image = models.ImageField(upload_to='post_and_products_images/')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'


class Company(models.Model):
    author = models.ForeignKey(User, verbose_name='director', related_name='companies', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='Company_logo/', blank=True, null=True)
    company_name = models.CharField(max_length=200)
    info = models.TextField(blank=True, null=True)
    # tel = PhoneNumberField(blank=True, help_text='Company phone number')
    company_email = models.EmailField(max_length=200, blank=True, null=True)
    telegram_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    url = models.SlugField(max_length=200, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'