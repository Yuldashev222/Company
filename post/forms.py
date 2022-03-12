from django.forms import ModelForm

from .models import *


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['post_category', 'title', 'post_image', 'post_text', 'tags', 'post_url']