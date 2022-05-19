from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class RegionForm(ModelForm):
    class Meta:
        model = models.Region
        fields = ('nom','biome','description')
        labels = {
            'nom' : _('Nom de région'),
            'biome' : _('Type de biome'),
            'description' : _('Description de la région'),
        }

class ChampForm(ModelForm):
    class Meta:
        model = models.Champ
        fields = ('region','alias','age','sexe','classification')
        labels = {
            'region' : _('Region'),
            'alias' : _('Alias'),
            'age' : _('Âge'),
            'sexe' : _('Sexe'),
            'classification': _('Histoire'),
        }