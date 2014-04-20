from django.test import TestCase
from django.test.client import RequestFactory
from factory import DjangoModelFactory
from .models import Trivia
from .views import AddGuesses


class TriviaFactory(DjangoModelFactory):
    FACTORY_FOR = Trivia


class TestAddMultipleGuesses(TestCase):

    def setUp(self):
        self.trivia = TriviaFactory()

    def test_if_no_guess_exists_a_single_empty_guess_appears(self):
        request = RequestFactory().get('/')
        request.session = {}
        view = AddGuesses.as_view()
        response = view(request, pk=self.trivia.id)
        self.assertContains(response, 'placeholder="enter a number"', count=1)

    def test_if_one_guess_exists_a_second_empty_guess_appears(self):
        request = RequestFactory().get('/')
        request.session = {'trivia-1': 3}
        view = AddGuesses.as_view()
        response = view(request, pk=self.trivia.id)
        self.assertContains(response, 'placeholder="enter a number"', count=2)
