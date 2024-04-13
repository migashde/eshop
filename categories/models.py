from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.CharField(max_length=200)
