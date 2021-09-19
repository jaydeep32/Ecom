from django.contrib import admin
from cart.models import Cart, OrderItem


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'qty', 'created_at', 'user', 'ordered', ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'ordered_date', 'ordered', ]

