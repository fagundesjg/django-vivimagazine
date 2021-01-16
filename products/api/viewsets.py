from rest_framework import viewsets

from products.models import Category, Product
from products.api.serializers import CategoriesSerializer, ProductsSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
