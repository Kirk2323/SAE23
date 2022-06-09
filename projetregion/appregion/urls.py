from django.urls import path

from . import views

urlpatterns = [
    path('ajout/',views.ajout),

    path('index2.html',views.index2),
    path('ajout/index2.html',views.index2),
    path('ajout2/index2.html',views.index2),


    path('ajout2/',views.ajout2),
    path('ajoutservice/',views.ajoutservice),
    path('ajoutappli/',views.ajoutappli),
    path('traitement2/',views.traitement2),
    path('traitement3/',views.traitement3),
    path('traitementservice/',views.traitementservice),
    path('',views.index),
    path('ch/',views.index),
    path('affiche/<int:id>/',views.affiche),
    path('affiche2/<int:id>/',views.affiche2),
    path('afficheservice/<int:id>/',views.afficheservice),
    path('afficheappli/<int:id>/',views.afficheappli),

    path('update/<int:id>/',views.update),
    path('update2/<int:id>/', views.update2),
    path('updateservice/<int:id>/',views.updateservice),
    path('updateappli/<int:id>/',views.updateappli),

    path('updatetraitement//',views.traitement2),
    path('updatetraitement/<int:id>/',views.updatetraitement),


    path('updatetraitement2/<int:id>/',views.updatetraitement2),
    path('updatetraitement2//',views.traitement3),

    path('updatetraitementservice/<int:id>/',views.updatetraitementservice),
    path('updatetraitementservice//',views.updatetraitementservice),

    path('updatetraitementappli/<int:id>/',views.updatetraitementappli),
    path('updatetraitementappli//',views.updatetraitementappli),

    path('delete/<int:id>/',views.delete),
    path('delete2/<int:id>/',views.delete2),
    path('deleteservice/<int:id>/',views.deleteservice),
    path('deleteappli/<int:id>/',views.deleteappli),
]


