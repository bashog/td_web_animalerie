from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('ajouter-un-animal/', views.add_animal, name='add_animal'),
    path('regle/', views.regle, name='regle'),
    path('animal/<str:id_animal>/', views.animal_detail, name='animal_detail'),
    path('equipement/<str:id_equipement>/', views.equipement_detail, name='equipement_detail'),
]