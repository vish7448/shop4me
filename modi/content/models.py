from django.db import models

# Create your models here.
class shoes_mo(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    disc = models.CharField(max_length=150)
    price = models.IntegerField()
    product_image = models.ImageField(null=True)
    shop_url = models.URLField(default=True)


class mobile(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    disc = models.CharField(max_length=150)
    price = models.IntegerField()
    product_image = models.ImageField(null=True)
    shop_url = models.URLField(default=True)

class baby_mo(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    disc = models.CharField(max_length=150)
    price = models.IntegerField()
    product_image = models.ImageField(null=True)
    shop_url = models.URLField(default=True)
class footwear_mo(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=150)
    disc = models.CharField(max_length=150)
    price = models.IntegerField()
    product_image = models.ImageField(null=True)
