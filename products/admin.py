from django.contrib import admin
from products.models import Product, SubCategory, Category

admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Category)
