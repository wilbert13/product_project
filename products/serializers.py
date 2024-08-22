from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'code', 'description', 'price', 'product_type']

    def validate_price(self, value):
        if value < 100:
            raise serializers.ValidationError("El precio mínimo debe ser 100 pesos.")
        return value

    def validate_product_type(self, value):
        if value not in ['local', 'international']:
            raise serializers.ValidationError("El tipo de producto debe ser 'local' o 'international'.")
        return value
