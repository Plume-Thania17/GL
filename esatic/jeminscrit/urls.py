from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('inscription/', views.inscription, name='inscription'),
    path('confirmation/<int:candidat_id>/', views.confirmation, name='confirmation'),
    path('imprimer/<int:candidat_id>/', views.imprimer_confirmation, name='imprimer_confirmation'),
]