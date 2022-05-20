from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id','title', 'price', 'description', 'sale_price', 'discount']

    def get_discount(self, obj):
        return obj.get_discount()













