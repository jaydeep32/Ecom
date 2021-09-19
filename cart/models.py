from django.db import models
from django.conf import settings

from product.models import Product

User = settings.AUTH_USER_MODEL


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    items = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(blank=True, null=True)
    ordered = models.BooleanField(default=False)

    def get_total_qty(self):
        items = self.items.all()
        total = 0
        for item in items:
            if not item.ordered:
                total += item.qty
        return total

    def save_order(self):
        for item in self.items.all():
            item.ordered = True
            item.save()
        self.ordered = True
        self.save()
        # return self

    def __str__(self):
        return f'This cart belongs to "{self.user}" user'
