# Generated by Django 5.0.6 on 2024-05-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='pid_for_home',
            field=models.IntegerField(default='0'),
        ),
    ]