# Generated by Django 5.2.1 on 2025-05-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_productstore_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_discount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
