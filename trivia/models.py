from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Trivia(models.Model):
    title = models.CharField(max_length=50)
    trivia = models.CharField(max_length=256)
    overview = models.TextField()
    insider = models.TextField(verbose_name='Insider Knowledge')
    details = models.TextField()


class Guess(models.Model):
    value = models.FloatField()
    trivia = models.ForeignKey(Trivia)
    user = models.ForeignKey(Player)
    placed = models.BooleanField(default=False)
    date_placed = models.DateTimeField(editable=False)

    class Meta:
        verbose_name_plural = 'Guesses'
