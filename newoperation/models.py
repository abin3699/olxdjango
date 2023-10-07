from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class OlxNew(models.Model):
    name =models.CharField(max_length=200)
    brand =models.CharField(max_length=200)
    modelyr =models.PositiveIntegerField()
    types =models.CharField(max_length=200)
    owner =models.CharField(max_length=200)
    km =models.PositiveIntegerField()
    price =models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    

