from django.contrib import admin
from django.urls import path
from . import views






urlpatterns = [
    path('', views.index, name='home-page'),

    path('catalog/', views.catalog, name='catalog-page'),
    path('catalog/<slug:category_slug>', views.category, name='category-page'),
    path('catalog/<slug:category_slug>/<slug:product_slug>/', views.product, name='product-page'),

    path('company/', views.company, name='company-page'),
    path('company/awards/', views.awards, name='awards-page'),
    path('company/technologies/', views.technologies, name='technologies-page'),

    path('clients/', views.clients, name='clients-page'),
    path('clients/payment/', views.payment, name='payment-page'),
    path('clients/delivery/', views.delivery, name='delivery-page'),

    path('contacts/', views.contacts, name='contacts-page'),
]





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