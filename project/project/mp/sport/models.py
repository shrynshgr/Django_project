from django.db import models

# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    contact = models.IntegerField(default=0)
    sport = models.CharField(max_length=25)
    mem = models.CharField(max_length=20)
    add = models.CharField(max_length=50)