from django.db import models
from enum import Enum
from uuid import uuid4


class Category(models.Model):
    id_category = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id_product = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64)
    price = models.FloatField()
    discount = models.IntegerField(null=True, blank=True)
    image1 = models.ImageField(upload_to="products")
    image2 = models.ImageField(upload_to="products", null=True, blank=True)
    image3 = models.ImageField(upload_to="products", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=1,
                              choices=(("M", "Masculino"), ("F", "Feminino")), default="M")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
