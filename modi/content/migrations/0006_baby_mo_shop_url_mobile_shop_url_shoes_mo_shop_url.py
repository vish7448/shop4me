# Generated by Django 4.0.3 on 2022-06-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_baby_mo_footwear_mo_shoes_mo_delete_shoes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baby_mo',
            name='shop_url',
            field=models.URLField(default=True),
        ),
        migrations.AddField(
            model_name='mobile',
            name='shop_url',
            field=models.URLField(default=True),
        ),
        migrations.AddField(
            model_name='shoes_mo',
            name='shop_url',
            field=models.URLField(default=True),
        ),
    ]
