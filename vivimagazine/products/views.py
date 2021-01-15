from django.views.generic import ListView

from products.models import Product


class ProductList(ListView):
    model = Product
