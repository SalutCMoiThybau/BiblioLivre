from django.db import models
from clients.models import Client
from books.models import Livre

# Create your models here.
class Emprunt(models.Model):
    STATUS = (
        ('emprunté', 'emprunté'),
        ('non rendu', 'non rendu'),
        ('rendu', 'rendu')
    )
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    livre = models.ForeignKey(Livre, null=True, on_delete=models.SET_NULL)
    date_debut_emprunt = models.DateField(max_length=10, null=True)
    date_fin_emprunt = models.DateField(max_length=10, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)

    def __str__(self):
        return f"Emprunt du {self.date_debut_emprunt} à {self.date_fin_emprunt} ({self.status})"
