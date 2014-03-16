from datetime import datetime
from django.contrib import messages
from django import forms
from django.views.generic import ListView
from django.views.generic.edit import FormView
from models import Trivia, Player, Guess


class TriviaList(ListView):
    model = Trivia

    def post(self, request, *args, **kwargs):
        guesses = request.POST.copy()
        guesses.pop('csrfmiddlewaretoken')
        # Add all the guesses into the session so they persist
        request.session.clear()
        for key, value in guesses.iteritems():
            if value:
                request.session[key] = value
        number_of_guesses = len(request.session.items())
        messages.add_message(request,
                             messages.SUCCESS,
                             str(number_of_guesses) + ' guesses saved')
        return super(TriviaList, self).get(request, *args, **kwargs)


class TriviaCheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


class TriviaCheckout(ListView, FormView):
    model = Trivia
    template_name = 'trivia/trivia_checkout.html'
    form_class = TriviaCheckoutForm
    success_url = 'http://www.bikeandbuild.org/cms/component/option,com_wrapper/Itemid,118/?item_name_1=7212'  # nopep8

    def dispatch(self, request, *args, **kwargs):
        # Needed if form is invalid
        self.object_list = self.get_queryset()
        self.session_keys = request.session.items()
        return super(TriviaCheckout, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TriviaCheckout, self).get_context_data(**kwargs)
        number_of_guesses = len(self.session_keys)
        suggested_donation = number_of_guesses * 10
        context.update({
            'number_of_guesses': number_of_guesses,
            'suggested_donation': suggested_donation,
        })
        return context

    def _save_guesses(self, player):
        guesses = []
        for key, value in self.session_keys:
            trivia_id = None
            splits = key.split('-')
            if splits[0] == 'trivia':
                trivia_id = splits[1]
            if trivia_id:
                trivia = Trivia.objects.get(pk=int(trivia_id))
                guess = Guess.objects.create(value=value,
                                             trivia=trivia,
                                             user=player,
                                             date_placed=datetime.now())
                guesses.append(guess)
        return guesses

    def form_valid(self, form):
        # Save the user
        player, created = \
            Player.objects.get_or_create(email=form.cleaned_data['email'])
        player.name = form.cleaned_data['name']
        player.save()
        # Save the guesses
        guesses = self._save_guesses(player)
        # Email the guesses to jeff & user
        #self._send_email(player, guesses)
        return super(TriviaCheckout, self).form_valid(form)
