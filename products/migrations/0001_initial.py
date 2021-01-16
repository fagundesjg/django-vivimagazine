# Generated by Django 3.1.5 on 2021-01-16 20:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('price', models.FloatField()),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('image1', models.ImageField(upload_to='products')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products')),
                ('description', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]