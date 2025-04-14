from django.urls import path
from Categorie.views import test, List_Categorie, places, ajouter


urlpatterns = [
    path("", test, name="test"),
    path('categories', List_Categorie, name='categories'),
    path('categories/<int:categorie_id>', places, name='places'),
    path("categories/<int:categorie_id>/ajouter", ajouter, name='ajouter')
]
