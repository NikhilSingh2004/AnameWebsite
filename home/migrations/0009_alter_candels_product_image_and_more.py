# Generated by Django 4.2 on 2023-04-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_candels_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candels',
            name='product_image',
            field=models.FileField(default='', null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='candels',
            name='product_title',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resignart',
            name='product_title',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
