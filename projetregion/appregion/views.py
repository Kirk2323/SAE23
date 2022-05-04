from django.shortcuts import render, HttpResponseRedirect
from .forms import RegionForm
from .forms import ChampForm
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
        return HttpResponseRedirect("/appregion/", {"region" : region})
    else :
        return render(request, "appregion/ajout.html", {"form": rform})

def traitement3(request):
    cform = ChampForm(request.POST)
    if cform.is_valid():
        champion = cform.save()
        return HttpResponseRedirect("/appregion/", {"champion" : champion})
    else :
        return render(request, "appregion/ajout2.html", {"form": cform})

def ajout(request):
    if request.method == "POST":
        form = RegionForm(request)
        return render(request,"appregion/ajout.html",{"form" : form})
    else :
        form = RegionForm()
        return render(request, "appregion/ajout.html", {"form" : form})

def ajout2(request):
    if request.method == "POST":
        form = ChampForm(request)
        return render(request,"appregion/ajout2.html",{"form" : form})
    else :
        form = ChampForm()
        return render(request, "appregion/ajout2.html", {"form" : form})

def index(request):
    liste = list(models.Region.objects.all())
    liste2 = list(models.Champ.objects.all())
    return render(request,"appregion/index.html",{"liste" : liste,"liste2" : liste2})



def affiche(request, id):
    region =models.Region.objects.get( pk = id)
    return render(request,"appregion/affiche.html", {"region" : region})

def affiche2(request, id):
    region =models.Region.objects.get( pk = id)
    return render(request,"appregion/affiche.html", {"region" : region})

def update(request, id):
    region = models.Region.objects.get(pk=id)
    form = RegionForm(region.dico())
    return render(request,"appregion/ajout.html",{"form":form, "id":id})

def update2(request, id):
    region = models.Region.objects.get(pk=id)
    form = RegionForm(region.dico())
    return render(request,"appregion/ajout.html",{"form":form, "id":id})

def updatetraitement(request, id):
    rform = RegionForm(request.POST)
    if rform.is_valid():
        region = rform.save(commit=False)
        region.id=id
        region.save()
        return HttpResponseRedirect("/appregion/")
    else:
        return render(request, 'appregion/ajout.html', {'form': rform,"id" : id})

def updatetraitement2(request, id):
    cform = ChampForm(request.POST)
    if cform.is_valid():
        champion = cform.save(commit=False)
        champion.id=id
        champion.save()
        return HttpResponseRedirect("/appregion/")
    else:
        return render(request, 'appregion/ajout2.html', {'form': cform,"id" : id})

def delete(request, id):
    region = models.Region.objects.get(pk=id)
    region.delete()
    return HttpResponseRedirect("/appregion/")

def delete2(request, id):
    champion = models.Champ.objects.get(pk=id)
    champion.delete()
    return HttpResponseRedirect("/appregion/")