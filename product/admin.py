from django.contrib import admin
from product.models import Product, Category, SubCategory, Color, Size


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'image', 'slug',
                    'price', 'in_stock', 'in_active', 'created_by']


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Color)
admin.site.register(Size)
