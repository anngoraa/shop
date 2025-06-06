# Generated by Django 5.2.1 on 2025-05-15 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_product_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='price_discount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[(1, 'Алкоголь'), (0, 'Еда')], default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
