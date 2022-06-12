from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'formula/index.html', {})

def catalog(request):
    return render(request, 'formula/catalog.html', {})

def company(request):
    return render(request, 'formula/company.html', {})

def awards(request):
    return render(request, 'formula/awards.html', {})

def technologies(request):
    return render(request, 'formula/technologies.html', {})

def clients(request):
    return render(request, 'formula/clients.html', {})

def payment(request):
    return render(request, 'formula/payment.html', {})

def delivery(request):
    return render(request, 'formula/delivery.html', {})

def contacts(request):
    return render(request, 'formula/contacts.html', {})






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