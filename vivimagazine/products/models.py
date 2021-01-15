from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    discount = models.IntegerField()
    image1 = models.ImageField(upload_to="products")
    image2 = models.ImageField(upload_to="products")
    image3 = models.ImageField(upload_to="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
