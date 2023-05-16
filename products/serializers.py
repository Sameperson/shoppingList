# serializers.py
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import Product, ProductList, ProductEntry


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductEntrySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    product_list = serializers.PrimaryKeyRelatedField(read_only=True)
    product_list_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = ProductEntry
        fields = '__all__'

    def create(self, validated_data):
        product_id = validated_data.pop('product_id', None)
        product_list_id = validated_data.pop('product_list_id', None)
        if product_id:
            product = Product.objects.get(id=product_id)
            validated_data['product'] = product
        if product_list_id:
            product_list = ProductList.objects.get(id=product_list_id)
            validated_data['product_list'] = product_list
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProductListSerializer(serializers.ModelSerializer):
    entries = ProductEntrySerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = ProductList
        fields = ['id', 'name', 'description', 'date', 'user', 'entries']
