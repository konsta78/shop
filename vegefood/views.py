from django.shortcuts import render
from django.views import View
from .settings.base import INFO
from .models import Product, User, Coupon, Cart

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework import status
from .serializers import UserSerializer, ProductSerializer, CouponSerializer, CartSerializer

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


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        filter_params = {param: request.GET[param] for param in request.GET}
        queryset = self.get_queryset()
        filter_queryset = queryset.filter(**filter_params)
        serializer = self.get_serializer(filter_queryset, many=True)
        return Response(serializer.data)


class CouponViewSet(ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CartViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.filter(user=kwargs['pk']), many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def add(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        user = User.objects.get(pk=request.GET['user'])
        count = request.GET['count']

        queryset = self.get_queryset()
        serializer = self.get_serializer(data=dict(user=user.pk, product=product.pk, count=count))
        serializer.is_valid(raise_exception=True)
        queryset.create(user=user, product=product, count=count)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)