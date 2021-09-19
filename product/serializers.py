from rest_framework import serializers
from product.models import Product, Category, SubCategory, Color, Size


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class GetProductSerializer(serializers.ModelSerializer):
    # color = ColorSerializer()
    # size = SizeSerializer()
    color = serializers.StringRelatedField(read_only=True)
    size = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
