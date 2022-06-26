from django.db import models

# Create your models here.
class deteail(models.Model):
    user_name = models.CharField(max_length=50)
    user_email=models.EmailField()
    password = models.CharField(max_length=20)
