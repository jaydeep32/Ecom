from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from cart.models import Cart
from order.models import Order, BillingAddress, Coupon
from order.serializers import BillingAddressSerializer, CouponSerializer, OrderSerializer


class BillingAddressList(ModelViewSet):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    http_method_names = ['get', 'put', 'post', 'delete']
    permission_classes = [IsAuthenticated, ]


class CouponList(ModelViewSet):
    http_method_names = ['get', 'delete']
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated, ]


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cart': openapi.Schema(type=openapi.TYPE_INTEGER, description='integer'),
        'coupon_code': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    },
    required=['cart'],
))
@api_view(['post'])
def complete_order(request):
    data = request.data
    try:
        billing_address = BillingAddress.objects.get(user=request.user)
    except ObjectDoesNotExist as e:
        return Response({'detail': 'Your billing details is\'t available..'})

    coupon_code = data.get('coupon_code')
    if coupon_code:
        try:
            coupon = Coupon.objects.get(code=coupon_code)
        except ObjectDoesNotExist as e:
            return Response({'detail': 'Coupon code does\'t exist..'})
    cart = get_object_or_404(Cart, id=data.get(
        'cart'), ordered=False, user=request.user)
    cart.save_order()
    order = Order.objects.create(
        user=request.user, cart=cart, billing_address=billing_address)
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_200_OK)
