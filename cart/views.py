from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from cart.models import Cart, OrderItem
from product.models import Product
from cart.serializers import CartSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CartList(ModelViewSet):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    http_method_names = ['get', 'post', 'delete']

    def get_queryset(self, *args, **kwargs):
        user = self.request.user if self.request.user.is_authenticated else 0
        return get_list_or_404(Cart, user__id=user)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'item': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
        }
    ))
    def create(self, request, *args, **kwargs):
        data = request.data
        product = get_object_or_404(Product, id=data.get('item'))
        cart, created = Cart.objects.get_or_create(
            user=request.user, ordered=False)
        orderitem, created = OrderItem.objects.get_or_create(
            product=product, user=request.user, ordered=False)
        if not created:
            orderitem.qty += 1
            orderitem.save()
        cart.items.add(orderitem)
        cart.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)


@swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'orderitem': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
    }
))
@api_view(['put'])
def add_qty(request):
    data = request.data
    order_item = get_object_or_404(
        OrderItem, id=data.get('orderitem'), ordered=False)
    cart = get_object_or_404(Cart, user=request.user, ordered=False)
    if order_item in cart.items.all():
        order_item.qty += 1
        order_item.save()
        return Response({'msg': 'item quantity is updated..'})
    return Response({'msg': 'you don\'t have this item in your cart..'})


@swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'orderitem': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
    }
))
@api_view(['put'])
def remove_qty(request):
    data = request.data
    order_item = get_object_or_404(
        OrderItem, id=data.get('orderitem'), ordered=False)
    cart = get_object_or_404(Cart, user=request.user, ordered=False)
    if order_item in cart.items.all():
        order_item.qty -= 1
        order_item.save()
        if order_item.qty <= 0:
            cart.items.remove(order_item)
            order_item.delete()
        return Response({'msg': 'item quantity is updated..'})
    return Response({'msg': 'you don\'t have this item in your cart..'})


@api_view(['post'])
@permission_classes([IsAuthenticated, ])
def cart_total_item(request):
    user = request.user if request.user.is_authenticated else 0
    cart = get_object_or_404(
        Cart, user=user, ordered=False)
    qty = cart.get_total_qty()
    return Response({
        'total_qty': qty,
    }, status=status.HTTP_200_OK)
