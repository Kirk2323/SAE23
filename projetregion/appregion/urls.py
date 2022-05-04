from django.urls import path

from . import views

urlpatterns = [
    path('bonjour/',views.bonjour),
    path('saisie/',views.saisie),
    path('traitement/',views.traitement),
    path('ajout/',views.ajout),
    path('ajout2/',views.ajout2),
    path('traitement2/',views.traitement2),
    path('traitement3/',views.traitement3),
    path('',views.index),
    path('ch/',views.index),
    path('affiche/<int:id>/',views.affiche),
    path('affiche2/<int:id>/',views.affiche2),

    path('update/<int:id>/',views.update),
    path('update2/<int:id>/', views.update2),

    path('updatetraitement//',views.traitement2),
    path('updatetraitement/<int:id>/',views.updatetraitement),

    path('updatetraitement2/<int:id>/',views.updatetraitement2),
    path('updatetraitement2//',views.traitement3),

    path('delete/<int:id>/',views.delete),
    path('delete2/<int:id>/',views.delete2),
]

