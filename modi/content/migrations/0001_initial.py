# Generated by Django 4.0.2 on 2022-05-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoes_name', models.CharField(max_length=15)),
                ('shoes_category', models.CharField(max_length=15)),
                ('shoes_disc', models.CharField(max_length=15)),
                ('shoes_price', models.IntegerField()),
            ],
        ),
    ]
