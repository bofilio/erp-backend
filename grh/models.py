from django.db import models
from django.contrib.auth.models import User
from config.base import BaseModel
# Create your models here.

class Structure(BaseModel):
    lebel=models.CharField(max_length=255)
    str_mere=models.ForeignKey(to="self",on_delete=models.PROTECT)
    email=models.EmailField()

class Employe(BaseModel):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    email=models.EmailField()
    user=models.OneToOneField(to=User, on_delete=models.PROTECT)
    structure=models.ForeignKey(to=Structure, on_delete=models.PROTECT)
