from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=6)
    image = models.ImageField(upload_to='users')
    email = models.EmailField(unique=True)