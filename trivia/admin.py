from django.contrib import admin
from .models import Player, Trivia, Guess


class TriviaAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'trivia')


class PlayerGuessesInline(admin.TabularInline):
    model = Guess
    extra = 0
    readonly_fields = ('date_placed',)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'email')
    inlines = [
        PlayerGuessesInline,
    ]


class GuessAdmin(admin.ModelAdmin):
    list_display = ('trivia',
                    'user',
                    'value')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Trivia, TriviaAdmin)
admin.site.register(Guess, GuessAdmin)
