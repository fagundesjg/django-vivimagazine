from rest_framework import serializers

from products.models import Category, Product


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"