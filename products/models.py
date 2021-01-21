from django.db import models
from django.http import JsonResponse
from enum import Enum
from uuid import uuid4


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class SubCategory(models.Model):
    class Meta:
        verbose_name = 'Sub-Categoria'
        verbose_name_plural = 'Sub-Categorias'

    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.name + " - " + self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64)
    price = models.FloatField()
    discount = models.IntegerField(null=True, blank=True)
    image1 = models.ImageField(upload_to="products")
    image2 = models.ImageField(upload_to="products", null=True, blank=True)
    image3 = models.ImageField(upload_to="products", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quant = models.IntegerField(default=0)
    gender = models.CharField(max_length=1,
                              choices=(("M", "Masculino"), ("F", "Feminino")), default="M")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def category(self):
        data = Category.objects.get(
            id=self.subcategory.category.id)
        return data.as_dict()

    def __str__(self):
        return self.name
