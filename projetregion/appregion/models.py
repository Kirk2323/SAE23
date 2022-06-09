from django.db import models

# Create your models here.

class Region(models.Model):
    nom = models.CharField(max_length=50)
    biome = models.CharField(max_length=50)
    description = models.TextField(null = True,blank = True)

    def __str__(self):
        chaine = f"Région de {self.nom}"#, biome {self.biome}, voici la description de cette région : {self.description}"
        return chaine

    def dico(self):
        return{'nom':self.nom,'biome':self.biome,'description':self.description}

class Champ(models.Model):
    region = models.ForeignKey("Region",on_delete=models.CASCADE, default=None)
    alias = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sexe = models.CharField(max_length=50)
    classification = models.TextField(blank = False)

    def __str__(self):
        chaine2 = f"Le champion {self.alias}"#Alias : {self.alias}, Âge : {self.age}, Sexe : {self.sexe}, Classification {self.classification}, champion de la région de {self.region.nom}"
        return chaine2

    def dico(self):
        return{'region' : self.region.nom, 'alias' : self.alias,'age' : {self.age}, 'sexe' : self.sexe, 'classification': self.classification}

class appli(models.Model):
    id = models.CharField(primary_key=True,max_length=200),
    name_app = models.CharField(max_length=50)
    logo = models.ImageField(blank=True)
    serveur = models.CharField(max_length=50)
    utilisateur = models.CharField(max_length=50)

    def dico(self):
        return {'id': self.id,'name_app': self.name_app,'logo': self.logo, 'serveur': self.serveur, 'utilisateur':self.utilisateur}


class service(models.Model):
    id = models.CharField(max_length=50,primary_key=True)
    nom_service = models.CharField(max_length=200)
    date_lancement = models.DateField(blank=True, null = True)
    mem = models.IntegerField(blank=False)
    mem_vive = models.IntegerField(blank=False)
    serveur_lancement = models.CharField(max_length=200)

    def dico(self):
        return {'id': self.id,'nom_service': self.nom_service,'date_lancement': self.date_lancement, 'mem': self.mem, 'mem_vive':self.mem_vive,'serveur_lancement':self.serveur_lancement}




