from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ("username", "email")


class EmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        fields = ['name', 'email', 'bio', 'photo', 'street', 'city', 'state']


class AddEmployeeForm(ModelForm):
    
    class Meta:
        model = Employee
        fields = ['user', 'name', 'email', 'position', 'bio', 'photo', 'telegram_link', 'instagram_link', 'facebook_link', 'street', 'city', 'state', 'url']


class UserForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'photo', 'first_name', 'last_name']
