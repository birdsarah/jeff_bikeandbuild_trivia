from os import path
from django.conf import settings
from django.views.generic import TemplateView
from django.core.exceptions import ImproperlyConfigured
from markdown import markdown


class StaticView(TemplateView):
    template_name = 'pages/static.html'

    def get_doc_path(self):
        if not self.doc_file:
            raise ImproperlyConfigured
        return path.abspath(
            path.join(settings.BASE_DIR, 'bikeandbuild', 'pages', self.doc_file))

    def render_markdown(self, mdfile):
        with open(mdfile, 'r') as f:
            return markdown(f.read())

    def get_context_data(self):
        context = super(StaticView, self).get_context_data()
        context.update({
            'standard': self.render_markdown(self.get_doc_path())
        })
        return context


class AboutView(StaticView):
    doc_file = 'About.md'


class SponsorsView(StaticView):
    doc_file = 'Sponsors.md'
