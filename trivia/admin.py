from django.contrib import admin
from .models import Player, Trivia, Guess


class TriviaAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'trivia')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email')


class GuessAdmin(admin.ModelAdmin):
    list_display = ('trivia',
                    'name',
                    'guess')

admin.site.register(Player)
admin.site.register(Trivia, TriviaAdmin)
admin.site.register(Guess)
