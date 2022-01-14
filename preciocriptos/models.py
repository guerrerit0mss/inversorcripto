from types import ClassMethodDescriptorType
from django.db import models
from django.db.models.base import Model

# Create your models here.


class Criptos (models.Model):
    tiker=models.CharField(max_length=10)
    nombre=models.CharField(max_length=20)