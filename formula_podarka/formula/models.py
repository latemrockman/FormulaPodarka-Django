from django.db import models
from django.utils.text import slugify
from .translit import text2translit

# Create your models here.

class Category(models.Model):
    name = models.CharField(default='', max_length=50)
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






