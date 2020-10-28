from django.db import models

# Create your models here.


class Product(models.Model):
    TYPE = (
        ('fruits', 'fruits'),
        ('vegetables', 'vegetables'),
        ('juices', 'juices'),
        ('dried', 'dried'),
    )

    name = models.CharField(max_length=20)
    image = models.CharField(max_length=20, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    price_dc = models.IntegerField()
    price_sale = models.IntegerField(null=True, blank=True)

    type = models.CharField(max_length=15, choices=TYPE)

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()


class Coupon(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    value = models.IntegerField()
    min_coast = models.IntegerField()
    start_at = models.DateField(auto_now_add=True)
    finish_at = models.DateField()


class Cart(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        unique_together = (('user', 'product'), )
