from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'photo']

@admin.register(Employee)
class EmployesAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'position', 'company', 'user', 'bio']