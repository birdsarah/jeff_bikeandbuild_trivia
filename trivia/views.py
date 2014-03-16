from django.contrib import messages
from django import forms
from django.views.generic import ListView
from django.views.generic.edit import FormView
from models import Trivia


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
        messages.add_message(request, messages.SUCCESS, str(number_of_guesses) + ' guesses saved')
        return super(TriviaList, self).get(request, *args, **kwargs)


class TriviaCheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


class TriviaCheckout(ListView, FormView):
    model = Trivia
    template_name = 'trivia/trivia_checkout.html'
    form_class = TriviaCheckoutForm
    success_url = 'http://www.bikeandbuild.org/cms/component/option,\
        com_wrapper/Itemid,118/?item_name_1=7212'

    def dispatch(self, request, *args, **kwargs):
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

    def post(self, request, *args, **kwargs):
        # Needed if form is invalid
        self.object_list = self.get_queryset()
        return super(TriviaCheckout, self).post(request, *args, **kwargs)
