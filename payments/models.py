
from django.conf import settings
from django.db import models
from order.models import Order

User = settings.AUTH_USER_MODEL


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='payment')
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    payment_id = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Create your models here.
