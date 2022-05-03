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