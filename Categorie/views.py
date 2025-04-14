from django.shortcuts import render, get_object_or_404, redirect
from .models import Categorie, Place
from .form import PlaceForm
from django.core.paginator import Paginator


def test(request):
  return render(request, 'landing.html')


def List_Categorie(request):
  categories = Categorie.objects.all()
  return render(request, 'categories.html', {"categories": categories})

def places(request, categorie_id):
  categorie = get_object_or_404(Categorie, id=categorie_id)
  places = Place.objects.filter(categorie=categorie)
  paginator = Paginator(places, 8)
  
  page_number = request.GET.get('page')  # Numéro de la page demandée
  page_obj = paginator.get_page(page_number)  # Obtenir les objets paginés
  
  if request.method == "GET":
    ville = request.GET.get("recherche")
    if ville is not None:
      page_obj = Place.objects.filter(ville__icontains= ville)
  
  context = {
    "categorie": categorie,
    "page_obj": page_obj,
  }
  return render(request, 'places.html',context)



def ajouter(request, categorie_id):     # vue pour ajouter un lieu en le liant directement à sa catégorie
  categorie = get_object_or_404(Categorie, id=categorie_id)
  
  if request.method == 'POST':
    form = PlaceForm(request.POST)
    if form.is_valid():
      place = form.save(commit=False)
      place.categorie = categorie
      place.save()
      return redirect("places", categorie_id=categorie.id)
    
  else:
    form = PlaceForm()
  
  context = {
    "form": form,
    "categorie": categorie,
  }
  return render(request, 'ajout.html', context)