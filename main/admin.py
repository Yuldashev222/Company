from django.contrib import admin
from .models import *


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
  list_display = ['id', 'image', 'product']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  list_display = ['id', 'company_name', 'author', 'category', 'company_email']

