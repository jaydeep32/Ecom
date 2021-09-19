from cart.models import Cart
from django.conf import settings
from django.db import models
from django_countries.fields import CountryField

User = settings.AUTH_USER_MODEL


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save_ortder(self, request):
        print(request)

    def __str__(self):
        return self.user.username


class BillingAddress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='biiling')
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    # country = CountryField()
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    # same_billing_address = models.BooleanField(max_length=100)
    # save_info = models.BooleanField(max_length=100)
    # payment_option = models.ChoiceField(max_length=100)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.IntegerField(default=0)
    exp_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code
