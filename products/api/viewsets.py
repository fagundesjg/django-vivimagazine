from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from products.models import Category, Product, SubCategory
from products.api.serializers import CategoriesSerializer, ProductsSerializer, SubCategoriesSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()


class SubcategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategoriesSerializer
    queryset = SubCategory.objects.all()


class ProductsViewSet(viewsets.ModelViewSet):
    __basic_fields = ('id', 'name')
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields
