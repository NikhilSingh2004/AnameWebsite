# Generated by Django 4.2 on 2023-04-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_candels_product_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('zip_code', models.IntegerField()),
            ],
        ),
    ]
