from django.urls import path

from . import views

urlpatterns = [
    path('bonjour/',views.bonjour),
    path('saisie/',views.saisie),
    path('traitement/',views.traitement),
    path('ajout/',views.ajout),
    path('traitement2/',views.traitement2),
    path('',views.index),
    path('affiche/<int:id>/',views.affiche),
    path('update/<int:id>/',views.update),
    path('updatetraitement/<int:id>/',views.updatetraitement),
    path('delete/<int:id>/',views.delete),
]