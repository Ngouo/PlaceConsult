from .models import Place
from django import forms


class PlaceForm(forms.ModelForm):
  localisation = forms.CharField(label='localisation', widget= forms.TextInput(attrs={'placeholder':
                                                                     "indication du lieu...",
                                                                     'style':'width:90%;'}))
  
  class Meta:
    model = Place
    fields = ["nom_lieu", "ville", 'localisation']