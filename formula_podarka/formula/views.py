from django.shortcuts import render
from .models import Category, Product, Technologies


# Create your views here.


def index(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')
    index_active = ' active'
    context = {
        'categories': categories,
        'products': products,
        'index_active': index_active
    }
    return render(request, 'formula/index.html', context)


def catalog(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')
    catalog_active = ' active'


    context = {
        'categories': categories,
        'products': products,
        'catalog_active': catalog_active
    }

    return render(request, 'formula/catalog.html', context)


def category(request, category_slug):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    category_id = Category.objects.get(slug=category_slug).id
    category_name = Category.objects.get(slug=category_slug).name.lower().capitalize()
    category_description = Category.objects.get(slug=category_slug).description
    products_of_category = Product.objects.filter(category_id=category_id)

    context = {
        'categories': categories,
        'products': products,
        'category_slug': category_slug,
        'products_of_category': products_of_category,
        'category_id': category_id,
        'category_name': category_name,
        'category_description': category_description
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
        'categories': categories,
        'products': products,
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
    company_active = ' active'


    context = {
        'categories': categories,
        'products': products,
        'company_active': company_active
    }
    return render(request, 'formula/company.html', context)


def awards(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'formula/awards.html', context)


def technologies(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')
    technologies = Technologies.objects.order_by('-id')



    context = {
        'categories': categories,
        'products': products,
        'technologies': technologies
    }
    return render(request, 'formula/technologies.html', context)



def technology(request, technology_slug):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')
    technologies = Technologies.objects.order_by('-id')


    technology_title = Technologies.objects.get(slug=technology_slug).title.lower().capitalize()
    technology_description = Technologies.objects.get(slug=technology_slug).description.lower().capitalize()





    context = {
        'categories': categories,
        'products': products,
        'technologies': technologies,
        'technology_slug': technology_slug,
        'technology_title': technology_title,
        'technology_description': technology_description

    }
    return render(request, 'formula/technology.html', context)



def clients(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')
    clients_active = ' active'

    context = {
        'categories': categories,
        'products': products,
        'clients_active': clients_active
    }
    return render(request, 'formula/clients.html', context)


def payment(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'formula/payment.html', context)


def delivery(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'formula/delivery.html', context)


def contacts(request):
    categories = Category.objects.order_by('-id')
    products = Product.objects.order_by('-id')
    contacts_active = ' active'

    context = {
        'categories': categories,
        'products': products,
        'contacts_active': contacts_active
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
