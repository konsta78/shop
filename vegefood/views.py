from django.shortcuts import render
from django.views import View
from .settings.base import INFO
from .models import Product

# Create your views here.


class IndexView(View):
    def get(self, request):
        context = INFO
        return render(request, 'vegefood/index.html', context)


class ShopView(View):
    def get(self, request):
        context = INFO
        context.update({'page_obj': Product.objects.all()})
        return render(request, 'vegefood/shop.html', context)
