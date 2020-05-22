from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from movies import forms
from django.contrib import messages
from .models import Movie
from django.urls import reverse_lazy

class MovieCreateView(CreateView):

    model = Movie
    form_class = forms.CreateMovieForm
    template_name = 'movie/movie_form.html'
    success_url = '/movie/list/'

    def form_valid(self, form, **kwargs):
        movie = form.save(commit=False)
        movie.save()
        messages.success(self.request, 'Movie added successfully!')
        return redirect(self.success_url) 


class MovieListView(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'

class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie:movie_list')

class MovieUpdateView(UpdateView):
    model = Movie
    form_class = forms.CreateMovieForm
    template_name = 'movie/movie_update_form.html'
    success_url = '/movie/list/'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'

