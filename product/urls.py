from rest_framework.routers import DefaultRouter
from product import views
from django.urls import path, include

route = DefaultRouter()
route.register('products', views.ProductList, basename='products')
route.register('color', views.Colors, basename='color')
route.register('size', views.Sizes, basename='size')

urlpatterns = [
    path('', include(route.urls)),
    # path('color/', views.Colors.as_view(), name='color'),
]
