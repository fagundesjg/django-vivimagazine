from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

from products.models import Category, Product, SubCategory
from products.api.serializers import CategoriesSerializer, ProductsSerializer, SubCategoriesSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'take'
    max_page_size = 100


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()


class SubcategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategoriesSerializer
    queryset = SubCategory.objects.all()


class ProductsViewSet(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ("gender", "subcategory", "subcategory__category")
    search_fields = ("name")
