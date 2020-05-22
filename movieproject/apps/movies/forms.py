from .models import Movie
from django import forms

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie','description','year','rating','cast']