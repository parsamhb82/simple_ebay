from django.db import models

from costumer.models import Costumer

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()