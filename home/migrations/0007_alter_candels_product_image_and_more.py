# Generated by Django 4.2 on 2023-04-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_candels_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candels',
            name='product_image',
            field=models.FileField(default='', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='resignart',
            name='product_image',
            field=models.FileField(default='', upload_to='media'),
        ),
    ]
