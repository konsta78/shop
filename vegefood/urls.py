"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import IndexView, ShopView, WishlistView, ProductSingleView, CartView, CheckoutView, \
    UserViewSet, ProductViewSet, CouponViewSet, CartViewSet
from rest_framework import routers

route = routers.SimpleRouter()
route.register(r'users', UserViewSet)
route.register(r'products', ProductViewSet)
route.register(r'coupons', CouponViewSet)
route.register(r'carts', CartViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('product_single/', ProductSingleView.as_view(), name='product_single'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

]

urlpatterns += route.urls
