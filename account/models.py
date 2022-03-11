from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(upload_to='img/Users/', blank=True, null=True)

    def __str__(self):
        return self.username


class Employee(models.Model):

    position__choices = [
        ('Pt', 'Post admin'),
        ('Pr', 'Product admin'),
    ]

    company = models.ForeignKey('main.Company', related_name='employee', on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='employee', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    email = models.EmailField(blank=True, null=True)
    position = models.CharField(max_length=2, choices=position__choices)
    bio = models.CharField(max_length=500, blank=True, null=True)
    photo = models.ImageField(upload_to='img/Employes/', blank=True, null=True)
    # tel = PhoneNumberField(blank=True, null=True)
    telegram_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    url = models.SlugField(unique=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employes'