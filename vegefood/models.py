from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=20)
    discount = models.IntegerField(null=True, blank=True)
    price_dc = models.IntegerField()
    price_sale = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
