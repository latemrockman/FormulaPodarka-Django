from django.contrib import admin
from .models import Product, Category

# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_per_page = 15

    readonly_fields = ['slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'article', 'price', 'category', 'slug']
    list_editable = ['article', 'price', 'category']
    list_per_page = 15
    search_fields = ['title']
    list_filter = ['category']


    fields = ['article', 'title', 'description', 'price', 'category', 'slug']

    readonly_fields = ['slug']
    #prepopulated_fields = {'slug': ('title',)}


