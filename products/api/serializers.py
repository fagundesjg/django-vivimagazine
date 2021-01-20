from rest_framework import serializers

from products.models import Category, SubCategory, Product


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_at", "updated_at"]


class SubCategoriesSerializer(serializers.ModelSerializer):
    # category = CategoriesSerializer(many=False, read_only=True)

    class Meta:
        model = SubCategory
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    subcategory = SubCategoriesSerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "discount", "image1", "image2", "image3",
                  "description", "quant", "gender", "created_at", "updated_at", "category", "subcategory"]
