from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from django.urls import path
from order import views

route = DefaultRouter()

route.register('billingaddress', views.BillingAddressList,
               basename='billingaddress')
route.register('coupon', views.CouponList, basename='coupon')

urlpatterns = [
    path('', include(route.urls)),
    path('complete_order/', views.complete_order, name='complete_order'),
]
