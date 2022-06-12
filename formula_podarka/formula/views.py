from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'formula/index.html', {})

def catalog(request):
    pass

def company(request):
    pass

def awards(request):
    pass

def technologies(request):
    pass

def clients(request):
    pass

def payment(request):
    pass

def delivery(request):
    pass

def contacts(request):
    pass






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