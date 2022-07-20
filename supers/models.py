from django.db import models

# Create your models here.
class Supers(models.Model):
    type = models.CharField(max_length=100)