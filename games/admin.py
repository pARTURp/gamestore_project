from django.contrib import admin
from .models import Genre, Game

class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'release_date')
    list_filter = ('genres', 'release_date')
    search_fields = ('title', 'developer', 'publisher')

admin.site.register(Genre)
admin.site.register(Game, GameAdmin)