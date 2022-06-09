from django.shortcuts import render, HttpResponseRedirect
from .forms import RegionForm
from .forms import ChampForm
from .forms import serviceForm
from .forms import appliForm
from . import models

# Create your views here.

def bonjour(request):
    return render(request,"appregion/base.html")


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

def ajoutservice(request):
    if request.method == "POST":
        form = serviceForm(request)
        return render(request,"appregion/ajoutservice.html",{"form" : form})
    else :
        form = serviceForm()
        return render(request, "appregion/ajoutservice.html", {"form" : form})

def ajoutappli(request):
    if request.method == "POST":
        form = appliForm(request)
        return render(request,"appregion/ajoutappli.html",{"form" : form})
    else :
        form = appliForm()
        return render(request, "appregion/ajoutappli.html", {"form" : form})

def index(request):
    liste = list(models.Region.objects.all())
    liste2 = list(models.Champ.objects.all())
    return render(request,"appregion/index.html",{"liste" : liste,"liste2" : liste2})

def index2(request):
    liste = list(models.Region.objects.all())
    liste2 = list(models.Champ.objects.all())
    return render(request, "appregion/index2.html", {"liste": liste, "liste2": liste2})


def affiche(request, id):
    region =models.Region.objects.get( pk = id)
    return render(request,"appregion/affiche.html", {"region" : region})

def affiche2(request, id):
    champ =models.Champ.objects.get( pk = id)
    return render(request,"appregion/affiche2.html", {"champ" : champ})

def afficheservice(request, id):
    service =models.service.objects.get( pk = id)
    return render(request,"appregion/afficheservice.html", {"service" : service})

def afficheappli(request, id):
    appli =models.appli.objects.get( pk = id)
    return render(request,"appregion/afficheappli.html", {"appli" : appli})

def update(request, id):
    region = models.Region.objects.get(pk = id)
    form = RegionForm(region.dico())
    return render(request,'appregion/ajout.html',{'form':form, 'id':id})

def update2(request, id):
    champ = models.Champ.objects.get(pk=id)
    form = ChampForm(champ.dico())
    return render(request,'appregion/ajout2.html',{'form':form, 'id':id})

def updateservice(request, id):
    service = models.service.objects.get(pk=id)
    form = serviceForm(service.dico())
    return render(request,'appregion/ajoutservice.html',{'form':form, 'id':id})

def updateappli(request, id):
    appli = models.appli.objects.get(pk=id)
    form = appliForm(appli.dico())
    return render(request,'appregion/ajoutappli.html',{'form':form, 'id':id})


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

def traitementservice(request):
    cform = serviceForm(request.POST)
    if cform.is_valid():
        service = cform.save()
        return HttpResponseRedirect("/appregion/", {"service" : service})
    else :
        return render(request, "appregion/ajoutservice.html", {"form": cform})

def traitementappli(request):
    cform = appliForm(request.POST)
    if cform.is_valid():
        appli = cform.save()
        return HttpResponseRedirect("/appregion/", {"appli" : appli})
    else :
        return render(request, "appregion/ajoutappli.html", {"form": cform})

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

def updatetraitementservice(request, id):
    cform = serviceForm(request.POST)
    if cform.is_valid():
        service = cform.save(commit=False)
        service.id=id
        service.save()
        return HttpResponseRedirect("/appregion/")
    else:
        return render(request, 'appregion/ajoutservice.html', {'form': cform,"id" : id})

def updatetraitementappli(request, id):
    cform = appliForm(request.POST)
    if cform.is_valid():
        appli = cform.save(commit=False)
        appli.id=id
        appli.save()
        return HttpResponseRedirect("/appregion/")
    else:
        return render(request, 'appregion/ajoutappli.html', {'form': cform,"id" : id})

def delete(request, id):
    region = models.Region.objects.get(pk=id)
    region.delete()
    return HttpResponseRedirect("/appregion/")

def delete2(request, id):
    champion = models.Champ.objects.get(pk=id)
    champion.delete()
    return HttpResponseRedirect("/appregion/")

def deleteservice(request, id):
    service = models.service.objects.get(pk=id)
    service.delete()
    return HttpResponseRedirect("/appregion/")

def deleteappli(request, id):
    appli = models.appli.objects.get(pk=id)
    appli.delete()
    return HttpResponseRedirect("/appregion/")