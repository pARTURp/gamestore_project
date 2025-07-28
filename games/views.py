from django.shortcuts import render, get_object_or_404
from .models import Game, Genre
from django.views.generic import ListView, DetailView

class GameListView(ListView):
    model = Game
    template_name = 'games/game_list.html'
    context_object_name = 'games'
    paginate_by = 9

    def get_queryset(self):
        genre_slug = self.kwargs.get('genre_slug')
        if genre_slug:
            genre = get_object_or_404(Genre, name=genre_slug)
            return Game.objects.filter(genres=genre)
        return Game.objects.all()

class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
    context_object_name = 'game'