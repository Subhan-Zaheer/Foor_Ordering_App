# Generated by Django 4.2 on 2023-08-04 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_product_measurement_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(default=None),
        ),
    ]
