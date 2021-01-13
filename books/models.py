from django.db import models

# Create your models here.
class Tag(models.Model):
    nom = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    ISBN = models.CharField(max_length=13, null=True)
    titre = models.CharField(max_length=200, null=True)
    nombre_pages = models.IntegerField(null=True)
    date_de_parution = models.DateField(max_length=10, null=True)
    maison_édition = models.CharField(max_length=50, null=True)
    auteur = models.CharField(max_length=50, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.titre} de {self.auteur} ({self.date_de_parution})"
