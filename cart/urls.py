from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from cart import views

route = DefaultRouter()
route.register('carts', views.CartList, basename='carts')

urlpatterns = [
    path('', include(route.urls), name='cart'),
    path('add_qty/', views.add_qty, name='add_qty'),
    path('remove_qty/', views.remove_qty, name='remove_qty'),
    path('cart_total_item/', views.cart_total_item, name='cart_total_item'),
]
