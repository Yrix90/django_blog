from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from .models import Movie


class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.object.all()
        return render(rquest, 'movies/movie_list.html', {'movies_list': movies})