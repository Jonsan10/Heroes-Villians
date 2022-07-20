from django.db import models
from supers.models import Supers

# Create your models here.

class HV(models.Model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    primary_ability = models.CharField(max_length=100)
    secondary_ability = models.CharField(max_length=100)
    catchphrase = models.CharField(max_length=100)
    super_type = models.ForeignKey(Supers, on_delete=models.CASCADE)