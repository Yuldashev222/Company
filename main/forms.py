from django.forms import ModelForm

from .models import *


class CompanyForm(ModelForm):
    
    class Meta:
        model = Company
        fields = ['category', 'company_name', 'logo', 'info', 'company_email', 'telegram_link', 'instagram_link', 'facebook_link', 'street', 'city', 'state', 'url']
