# Generated by Django 5.0.6 on 2024-05-09 21:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='StoreApp.category'),
        ),
    ]