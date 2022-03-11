from django.urls import path
from .views import *
from account.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('testimonial/', testimonials, name='testimonials'),
    path('services/', services, name='services'),
    path('products/', products, name='products'),
    path('pricing/', pricing, name='pricing'),
    path('post/', post, name='post'),
    path('contact/', contact, name='contact'),
    path('post-single/', post_single, name='post-single'),
    path('Login/', user_login, name='login'),
    path('Registration/', registration, name='registration'),
    path('logout/', log_out, name='logout'),
    path('profile_user/<str:username>/', profile_user, name='profile_user'),
    path('profile_employee/<slug:url>/', profile_employee, name='profile_employee'),
    path('edit_company/<slug:url>/', edit_company, name='edit_company'),
    path('<slug:url>/', delete_company, name='delete_company'),
]
