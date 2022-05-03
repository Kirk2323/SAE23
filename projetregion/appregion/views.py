from django.shortcuts import render, HttpResponseRedirect
from .forms import RegionForm
from . import models

# Create your views here.

def bonjour(request):
    return render(request,"appregion/bonjour.html")

def saisie(request):
    return render(request,"appregion/saisie.html")

def traitement(request):
    nom = request.POST["nom"]
    return render(request,"appregion/traitement.html",{"nom": nom})


def traitement2(request):
    rform = RegionForm(request.POST)
    if rform.is_valid():
        region = rform.save()
        return HttpResponseRedirect("/appregion/")
    else :
        return render(request, "appregion/ajout.html", {"form": rform})


def ajout(request):
    if request.method == "POST":
        form = RegionForm(request)
        return render(request,"appregion/ajout.html",{"form" : form})
    else :
        form = RegionForm()
        return render(request, "appregion/ajout.html", {"form" : form})

def index(request):
    liste = list(models.Region.objects.all())
    return render(request,"appregion/index.html",{"liste" : liste})


def affiche(request, id):
    region =models.Region.objects.get( pk = id)
    return render(request,"appregion/affiche.html", {"region" : region})

def update(request, id):
    region = models.Region.objects.get(pk=id)
    form = RegionForm(region.dico())
    return render(request,"appregion/ajout.html",{"form":form, "id":id})

def updatetraitement(request, id):
    rform = RegionForm(request.POST)
    if rform.is_valid():
        region = rform.save(commit=False)
        region.id = id
        region.save()
        return HttpResponseRedirect("/appregion/")
    else:
        return render(request, "appregion/ajout.html", {"form": rform,"id" : id})

def delete(request, id):
    region = models.Region.objects.get(pk=id)
    region.delete()
    return HttpResponseRedirect("/appregion/")