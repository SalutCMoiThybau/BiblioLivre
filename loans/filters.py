import django_filters
from .models import Emprunt

class EmpruntFiltre(django_filters.FilterSet):
    class Meta:
        model = Emprunt
        fields = '__all__'
        exclude = ['client']
