from django.db import models

# Create your models here.

class Region(models.Model):
    nom = models.CharField(max_length=50)
    biome = models.CharField(max_length=50)
    description = models.TextField(null = True,blank = True)

    def __str__(self):
        chaine = f"Région de {self.nom}, biome {self.biome}, voici la description de cette région : {self.description}"
        return chaine

    def dico(self):
        return{"nom":self.nom,"biome":self.biome,"description":self.description}

class Champ(models.Model):
    alias = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    sexe = models.TextField(max_length=50)
    classification = models.TextField(max_length=500)

    def __str__(self):
        chaine = f"Alias : {self.alias}, Âge : {self.age}, Sexe : {self.sexe}, Classification {self.classification}"
        return chaine

    def dico2(self):
        return{"Alias : {self.alias}, Âge : {self.âge}, Sexe : {self.sexe}, Classification {self.classification}"}