from django.db import models

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50, null=True)
    prenom = models.CharField(max_length=50, null=True)
    adresse_mail = models.EmailField(max_length=100, null=True)
    nombre_livres_possédés = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"
