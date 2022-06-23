from django.db import models
from django.utils.text import slugify
from .translit import text2translit

# Create your models here.

class Category(models.Model):
    name = models.CharField(default='', max_length=50)
    description = models.TextField(default='', max_length=800)
    slug = models.SlugField(default='', null=False, db_index=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(text2translit(self.name))
        super(Category, self).save(*args, **kwargs)



class Product(models.Model):
    article = models.IntegerField()
    title = models.CharField(default='', max_length=50)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    slug = models.SlugField(default='', null=False, db_index=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(text2translit(self.title))
        super(Product, self).save(*args, **kwargs)

class Info(models.Model):
    email = models.EmailField()
    telephone = models.CharField(default='', max_length=20)
    logo = models.CharField(default='', max_length=40)
    head_date = models.CharField(default='', max_length=10)
    head_date_title = models.CharField(default='', max_length=50)
    head_date_слоган = models.CharField(default='', max_length=50)

    company_name = models.CharField(default='', max_length=50)
    company_adress = models.CharField(default='', max_length=50)
    work_schedule = models.CharField(default='', max_length=50)
    legal_name = models.CharField(default='', max_length=50)
    inn = models.CharField(default='', max_length=50)
    ogrn = models.CharField(default='', max_length=50)
    legal_adress = models.CharField(default='', max_length=50)
    general_manager = models.CharField(default='', max_length=50)
    karta = models.CharField(default='', max_length=200)
    meta_tags = models.TextField()

class Tehnologies(models.Model):
    title = models.CharField('', max_length=30)
    description = models.TextField()

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'









