from django.db import models
from config.base import BaseModel
from grh.models import Structure,Employe
# Entuty model represente l'expéditeur en tant que structure ou une personne
class Entity(BaseModel):
    name=models.CharField(max_length=255)
    structure=models.OneToOneField(to=Structure, on_delete=models.PROTECT,null=True,blank=True)
    employe=models.OneToOneField(to=Employe,on_delete=models.PROTECT,null=True,blank=True)
    def getExpediteur(self):
        if(self.structure):
            return self.structure
        return self.employe
    class Meta:
        verbose_name="Expediteur"
    def __str__(self):
        return self.name

class TypeCourier(BaseModel):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Types"
        verbose_name = "Type"
    def __str__(self):
        return self.name

class Classification(BaseModel):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Status(BaseModel):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Statuts"
        verbose_name = "Statut"
    def __str__(self):
        return self.name



direction_choices=(
    ("arrivee","Arrivée"),
    ("depart","Départ")
)

class Courier(BaseModel):
    #fields
    objet=models.TextField(max_length=255)
    referance_exp=models.CharField(max_length=255, verbose_name="Réferance Expéditeur")
    n_enregistrement=models.CharField(max_length=255, verbose_name="N° Enrigestrement Local")
    direction=models.CharField(max_length=255, choices=direction_choices)
    date_arrivee=models.DateField()
    date_expedition=models.DateField()
    exige_reponse=models.BooleanField(default=False)
    instructions=models.TextField(null=True,blank=True)
    #relashinships
    expediteur = models.ForeignKey(to=Entity, on_delete=models.PROTECT,related_name="courier_envoyes")
    destinataires = models.ManyToManyField(Entity,related_name="couriers_recus")
    visible_a = models.ManyToManyField(Entity, related_name="couriers_visibles", verbose_name="Visible à")
    type = models.ForeignKey(to=TypeCourier, on_delete=models.PROTECT)
    classification = models.ForeignKey(to=Classification, on_delete=models.PROTECT)
    reponse = models.ForeignKey(to="self", null=True, blank=True, on_delete=models.DO_NOTHING)
    status=models.ForeignKey(to=Status, on_delete=models.PROTECT, verbose_name="Traitement")
    deleted=models.BooleanField(default=False,editable=False, verbose_name="Supprimé")


    def __str__(self):
        return self.objet


class Attachment(BaseModel):
    file=models.FileField()
    courier=models.ForeignKey(to=Courier, on_delete=models.CASCADE,related_name="attachments")
    name=models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.file.name

    def delete(self, using=None, keep_parents=False):
        # assuming that you use same storage for all files in this model:
        storage = self.file.storage
        if storage.exists(self.file.name):
            storage.delete(self.file.name)
        super().delete()






