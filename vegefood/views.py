from django.shortcuts import render
from django.views import View
from .settings.base import INFO
from .models import Product

# Create your views here.

context = INFO

class IndexView(View):
    def get(self, request):
        return render(request, 'vegefood/index.html', context)


class ShopView(View):
    def get(self, request):
        context.update({'page_obj': Product.objects.all()})
        return render(request, 'vegefood/shop.html', context)


class WishlistView(View):
    def get(self, request):
        return render(request, 'vegefood/wishlist.html', context)


class ProductSingleView(View):
    def get(self, request):
        return render(request, 'vegefood/product-single.html', context)


class CartView(View):
    def get(self, request):
        return render(request, 'vegefood/cart.html', context)


class CheckoutView(View):
    def get(self, request):
        return render(request, 'vegefood/checkout.html', context)
