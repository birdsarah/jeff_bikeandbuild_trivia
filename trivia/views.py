from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib import messages
from models import Trivia


class TriviaList(ListView):
    model = Trivia

    def post(self, request, *args, **kwargs):
        guesses = request.POST.copy()
        guesses.pop('csrfmiddlewaretoken')
        # Add all the guesses into the session so they persist
        for key, value in guesses.iteritems():
            request.session[key] = value
        messages.add_message(request, messages.SUCCESS, 'Guesses saved')
        return super(TriviaList, self).get(request, *args, **kwargs)


class TriviaCheckout(ListView, FormView):
    model = Trivia
    template_name = 'trivia/trivia_checkout.html'

