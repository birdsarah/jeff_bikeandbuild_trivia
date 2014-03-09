from django.views.generic import ListView
from .models import Trivia

class TriviaList(ListView):
        model = Trivia
