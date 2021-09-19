from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from product.models import Color, Product, Size
from product.serializers import ColorSerializer, ProductSerializer, GetProductSerializer, SizeSerializer


class MyPage(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'records'
    # max_page_size = 2


class ProductList(ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return GetProductSerializer
        return ProductSerializer

    queryset = Product.objects.all()
    permission_classes = [IsAdminUser, ]
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    filterset_fields = ['color', 'size']
    search_fields = ['$color', '^size']
    pagination_class = MyPage


class Colors(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    http_method_names = ['get', 'post']


class Sizes(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    http_method_names = ['get', 'post']
