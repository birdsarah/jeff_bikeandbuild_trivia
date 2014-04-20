from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    add_to_list = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Trivia(models.Model):
    title = models.CharField(max_length=50)
    trivia = models.CharField(max_length=256)
    unit = models.CharField(max_length=30)
    overview = models.TextField()
    insider = models.TextField(verbose_name='Insider Knowledge')
    details = models.TextField()
    image = models.ImageField(upload_to='trivia', null=True, blank=True)

    def __unicode__(self):
        return self.title


class Guess(models.Model):
    value = models.FloatField()
    trivia = models.ForeignKey(Trivia)
    user = models.ForeignKey(Player)
    placed = models.BooleanField(default=False)
    date_placed = models.DateTimeField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Guesses'

    def __unicode__(self):
        return ('%s %s %s') % (self.trivia, self.user, self.value)
