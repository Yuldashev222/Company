from random import choices
from django.forms import SelectDateWidget
from taggit.managers import TaggableManager
from django.db import models
from category.models import *
from account.models import *


class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey('main.Company', on_delete=models.CASCADE)
    author = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500)
    text = models.TextField()
    tags = TaggableManager(blank=True)
    image = models.ImageField(upload_to='post/')
    url = models.SlugField(unique=True)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

