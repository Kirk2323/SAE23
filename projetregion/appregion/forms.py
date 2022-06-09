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

class serviceForm(ModelForm):
    class Meta:
        model = models.service
        fields = ('id','nom_service','date_lancement','mem','mem_vive','serveur_lancement')
        labels = {
            'id':_('Id'),
            'nom_service':_('Nom_service'),
            'date_lancement':_('date_lancement'),
            'mem':_('mem'),
            'mem_vive':_('mem_vive'),
            'serveur':_('serveur_lancement'),
        }

class appliForm(ModelForm):
    class Meta:
        model = models.appli
        fields = ('id','name_app','logo','serveur','utilisateur')
        labels = {
            'id':_('Id'),
            'name_app':_('name_app'),
            'logo':_('logo'),
            'serveur':_('serveur'),
            'utilisateur':_('utilisateur'),
        }