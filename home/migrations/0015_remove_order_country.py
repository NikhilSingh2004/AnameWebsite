# Generated by Django 4.1.7 on 2023-04-09 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_order_product_no_alter_order_address_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
    ]
