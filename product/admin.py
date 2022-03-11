from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'price', 'author', 'company', 'date_created', 'date_updated']