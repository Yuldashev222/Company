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
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey('main.Company', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500)
    post_text = models.TextField()
    tags = TaggableManager(blank=True)
    post_image = models.ImageField(upload_to='post/')
    post_url = models.SlugField(unique=True)
    date_created = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_tag_names(self):
        return [tag.name for tag in Post.objects.get_for_object(self)]


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

