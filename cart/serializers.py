from rest_framework import serializers
from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    # items = serializers.StringRelatedField(many=True, read_only=True)
    # user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'
        # read_only_fields = ['user', 'start_date', 'ordered_date', 'ordered', ]


