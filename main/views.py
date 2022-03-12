from ast import Return
from itertools import product
from math import prod
from django.shortcuts import redirect, render

from .models import Company
from post.models import Post
from product.models import Product, Image


from .forms import CompanyForm
from post.forms import PostForm
from product.forms import ProductForm, ImageForm
from account.forms import AddEmployeeForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def services(request):
    return render(request, 'services.html')

def products(request):
    return render(request, 'products.html')

def pricing(request):
    return render(request, 'pricing.html')

def post(request):
    return render(request, 'post.html')

def contact(request):
    return render(request, 'contact.html')

def post_single(request):
    return render(request, 'post-single.html')


def delete_company(request, url):
    company = Company.objects.get(url=url)
    user = company.author

    company.delete()

    try:
        return redirect('profile_employee', user.employee.url)
    
    except:
        return redirect('profile_user', user.username)




def edit_company(request, url):
    company = Company.objects.get(url=url)

    company_form = CompanyForm(instance=company)

    add_post_form = PostForm()
    add_product_form = ProductForm()
    add_product_image_form = ImageForm()
    add_employee_form = AddEmployeeForm()

    posts = Post.objects.filter(company=company)
    products = Product.objects.filter(company=company)

    if request.POST:

        company_form = CompanyForm(request.POST or None, request.FILES or None, instance=company)

        add_product_form = ProductForm(request.POST or None, request.FILES or None)
        add_product_image_form = ImageForm(request.POST or None, request.FILES or None)
        add_post_form = PostForm(request.POST or None, request.FILES or None)
        add_employee_form = AddEmployeeForm(request.POST or None, request.FILES or None)

        if company_form.is_valid():
            obj = company_form.save(commit=False)
            obj.author = company.author
            obj.save()
        
        if add_post_form.is_valid():
            print('//////////////////////')
            obj = add_post_form.save(commit=False)
            obj.company = company
            obj.author = company.author
            obj.save()

            add_post_form.save_m2m()

        if add_product_form.is_valid() and add_product_image_form.is_valid():
            obj_product = add_product_form.save(commit=False)
            obj_product.company = company
            obj_product.author = company.author
            obj_product.save()
            
            obj_product_image = add_product_image_form.save(commit=False)
            obj_product_image.product = obj_product
            obj_product_image.save()

        if add_employee_form.is_valid():
            obj_emp = add_employee_form.save(commit=False)
            obj_emp.company = company
            obj_emp.save()
            
            

            return redirect('edit_company', url)

    context = {
        'company': company,
        'company_form': company_form,
        'add_post_form': add_post_form,
        'add_product_form': add_product_form,
        'add_product_image_form': add_product_image_form,
        'add_employee_form': add_employee_form,

        'posts': posts,
        'products': products,
    }

    return render(request, 'edit_company.html', context)


