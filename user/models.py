from order.models import BillingAddress
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    billing = models.ForeignKey(
        BillingAddress, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='none.png')

    def __str__(self):
        return self.user.username
