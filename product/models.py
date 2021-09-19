from django.db import models
from autoslug import AutoSlugField
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name


class Size(models.Model):
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='product', null=True, blank=True)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, related_name='product', null=True, blank=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    slug = AutoSlugField(populate_from='title', unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    color = models.ForeignKey(Color, models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(Size, models.SET_NULL, null=True, blank=True)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.title
