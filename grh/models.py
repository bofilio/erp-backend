from django.db import models
from django.contrib.auth.models import User
from config.base import BaseModel
# Create your models here.

class Structure(BaseModel):
    lebel=models.CharField(max_length=255)
    str_mere=models.ForeignKey(to="self",on_delete=models.PROTECT, null=True, blank=True)
    email=models.EmailField()
    def __str__(self):
        return self.lebel

class Employe(BaseModel):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    email=models.EmailField()
    user=models.OneToOneField(to=User, on_delete=models.PROTECT,related_name="the_employe")
    structure=models.ForeignKey(to=Structure, on_delete=models.PROTECT,related_name="employes")
    def __str__(self):
        return "{} {}".format(self.nom,self.prenom)
