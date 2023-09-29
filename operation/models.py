from django.db import models

# Create your models here.

class Olx(models.Model):
    name =models.CharField(max_length=200)
    brand =models.CharField(max_length=200)
    modelyr =models.PositiveIntegerField()
    types =models.CharField(max_length=200)
    owner =models.CharField(max_length=200)
    km =models.PositiveIntegerField()
    price =models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

