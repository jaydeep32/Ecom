from faker import Faker
from django.contrib.auth.models import User
from product.models import Product, Category
from django.core.management.base import BaseCommand
import random


fakegen = Faker()


class FakeProduct:

    def __init__(self):
        self.category = Category.objects.get(id=random.randint(1, 4))
        # print(self.category)
        self.user = User.objects.get(id=random.randint(1, 3))
        self.product()

    def product(self):
        product = Product.objects.create(
            category=self.category,
            title=fakegen.name(),
            author=fakegen.name(),
            description=fakegen.text(),
            image=fakegen.url(),
            slug=fakegen.slug(),
            price=fakegen.random.random()*100,
            in_stock=True,
            in_active=True,
            created_by=self.user,
        )
        return product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # for _ in range(2):
        # try:
        FakeProduct()
        # except:
        # pass
