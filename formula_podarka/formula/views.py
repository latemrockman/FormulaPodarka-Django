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


def category(request, category_slug):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    category_id = Category.objects.get(slug=category_slug).id
    category_name = Category.objects.get(slug=category_slug).name.lower().capitalize()
    products_of_category = Product.objects.filter(category_id=category_id)



    context = {
        'categories' : categories,
        'products'   : products,
        'category_slug': category_slug,
        'products_of_category': products_of_category,
        'category_id': category_id,
        'category_name': category_name
    }
    return render(request, 'formula/category.html', context)

def product(request, category_slug, product_slug):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    category_name = Category.objects.get(slug=category_slug).name.lower().capitalize()
    product_name = Product.objects.get(slug=product_slug).title.lower().capitalize()
    product_article = Product.objects.get(slug=product_slug).article
    product_description = Product.objects.get(slug=product_slug).description
    product_price = Product.objects.get(slug=product_slug).price


    context = {
        'categories' : categories,
        'products'   : products,
        'category_slug': category_slug,
        'product_slug': product_slug,
        'category_name': category_name,
        'product_name': product_name,
        'product_article': product_article,
        'product_description': product_description,
        'product_price': product_price
    }



    return render(request, 'formula/product.html', context)


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