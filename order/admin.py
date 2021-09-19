from django.contrib import admin
from order.models import Coupon, Order, BillingAddress


admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(BillingAddress)
