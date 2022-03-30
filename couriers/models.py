from django.db import models
from config.base import BaseModel

# Entuty peut etre un expediteur ou un destinataire
class Entity(BaseModel):
    name=models.CharField(max_length=255)
    email = models.CharField(max_length=255)
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
    def __str__(self):
        return self.objet


class Attachment(BaseModel):
    file=models.FileField()
    courier=models.ForeignKey(to=Courier, on_delete=models.CASCADE,related_name="files")
    def __str__(self):
        return self.file.name






