from django.shortcuts import render
from django.views import View
from .settings.base import INFO

# Create your views here.


class IndexView(View):
    def get(self, request):
        context = INFO
        return render(request, 'vegefood/index.html', context)


class ShopView(View):
    def get(self, request):
        d = {'page_obg': [
            {
                'image': ...,
                'name': ...,
                'discount': ...,
                'price_dc': ...,
                'price_sale': ...,
            }
        ]}
        return render(request, 'vegefood/shop.html')