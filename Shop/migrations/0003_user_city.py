# Generated by Django 5.2.1 on 2025-05-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
