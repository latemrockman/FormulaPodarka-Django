from django.db import models

# Create your models here.



class Product(models.Model):
    article = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

