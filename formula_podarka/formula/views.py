from django.shortcuts import render
from .models import Category, Product

# Create your views here.



def index(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')
    context = {
        'categories' : categories,
        'products'   : products
    }
    return render(request, 'formula/index.html', context)

def catalog(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories' : categories,
        'products'   : products
    }

    return render(request, 'formula/catalog.html', context)

def company(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories' : categories,
        'products'   : products
    }
    return render(request, 'formula/company.html', context)

def awards(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories' : categories,
        'products'   : products
    }
    return render(request, 'formula/awards.html', context)

def technologies(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories' : categories,
        'products'   : products
    }
    return render(request, 'formula/technologies.html', context)

def clients(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories' : categories,
        'products'   : products
    }
    return render(request, 'formula/clients.html', context)

def payment(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories' : categories,
        'products'   : products
    }
    return render(request, 'formula/payment.html', context)

def delivery(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories' : categories,
        'products'   : products
    }
    return render(request, 'formula/delivery.html', context)

def contacts(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories' : categories,
        'products'   : products
    }
    return render(request, 'formula/contacts.html', context)






"""
home
catalog
company
- awards
- technologies
clients
- payment
- delivery
contacts
"""