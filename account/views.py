from itertools import product
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import authenticate

from .forms import EmployeeForm, UserForm, UserRegistrationForm
from post.forms import PostForm
from post.models import Post
from product.forms import ProductForm
from main.forms import CompanyForm
from product.models import Product
from .models import *

def user_login(request):

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')

        else:
            messages.error(request, 'Login yoki parol xato Qaytadan urinib koring')

            return redirect('login')


    return render(request, 'login.html')


def log_out(request):
    logout(request)

    return redirect('home')


def registration(request):
    users = User.objects.all()
    form = UserRegistrationForm()

    if request.POST:
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            obj = form.cleaned_data.get('username')
            obj = form.save()

            return redirect('login')

        elif request.POST.get('username') in users:
            messages.error(request, 'bunday foydalanuvchi ro\'yxatdan o\'tgan')


            return redirect('registration')

        else:
            messages.error(request, 'Parol kamida 8 ta belgidan iborat bolishi kerak')

            return redirect('registration')

    return render(request, 'register.html')


def profile_employee(request, url):
    employee = Employee.objects.get(url=url)

    user_form = EmployeeForm(instance=employee)

    posts = Post.objects.filter(author=employee)
    products = Product.objects.filter(author=employee)

    add_post_form = PostForm()
    add_product_form = ProductForm()
    add_company_form = CompanyForm()

    if request.POST:
        user_form = EmployeeForm(request.POST or None, request.FILES or None, instance=employee)

        add_post_form = PostForm(request.POST or None, request.FILES or None)
        add_product_form = ProductForm(request.POST or None, request.FILES or None)
        add_company_form = CompanyForm(request.POST or None, request.FILES or None)

        if user_form.is_valid():
            obj = user_form.save(commit=False)
            obj.company = employee.company
            obj.user = request.user
            obj.save()

        if add_post_form.is_valid():
            obj = add_post_form.save(commit=False)
            obj.company = employee.company
            obj.author = request.user.employee
            obj.save()

        if add_product_form.is_valid():
            obj = add_product_form.save(commit=False)
            obj.company = employee.company
            obj.author = request.user.employee
            obj.save()

        if add_company_form.is_valid():
            obj = add_company_form.save(commit=False)
            obj.author = request.user
            obj.save()

            return redirect('profile_employee', url)
    

    context = {
        'user': employee,
        'user_for_companies': employee.user,


        'posts': posts,
        'products': products,

        'user_form': user_form,
        'add_post_form': add_post_form,
        'add_product_form': add_product_form,
        'add_company_form': add_company_form,

    }


    return render(request, 'profile.html', context)


def profile_user(request, username):
    user = User.objects.get(username=username)

    user_form = UserForm(instance=user)
    add_company_form = CompanyForm()        

    if request.POST:
        user_form = UserForm(request.POST or None, request.FILES or None, instance=user)
        add_company_form = CompanyForm(request.POST or None, request.FILES or None)

        if user_form.is_valid():
            obj = user_form.save(commit=False)
            obj.save()

        if add_company_form.is_valid():
            obj = add_company_form.save(commit=False)
            obj.author = request.user
            obj.save()

            return redirect('profile_user', username)

    context = {
        'user': user,
        'user_for_companies': user,

        'user_form': user_form,
        'add_company_form': add_company_form,
    }        


    return render(request, 'profile.html', context)
