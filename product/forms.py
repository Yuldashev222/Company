from django.forms import ModelForm

from .models import *


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['product_category', 'name', 'product_text', 'info', 'price', 'product_url', ]


class ImageForm(ModelForm):

    class Meta:
        model = Image
        fields = ['image']