# Generated by Django 5.0.6 on 2024-05-11 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0007_alter_user_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Enter a valid 16-digit card number.', regex='^\\d{16}$')])),
                ('expiration_date', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Enter a valid expiration date in MM/YY format.', regex='^(0[1-9]|1[0-2])\\/\\d{2}$')])),
                ('cvv', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='Enter a valid CVV.', regex='^\\d{3,4}$')])),
                ('billing_address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state_province', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('ordered_item', models.CharField(max_length=150)),
            ],
        ),
    ]
