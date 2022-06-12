from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(default='', max_length=50)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def __str__(self):
        return f'{self.name}'



class Product(models.Model):
    article = models.IntegerField()
    title = models.CharField(default='', max_length=50)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}'




