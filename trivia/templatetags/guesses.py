from django import template


def get_guess(trivia, session):
    session_key = '-'.join(('trivia', str(trivia.id)))
    return session.get(session_key, '')

register = template.Library()
register.filter('get_guess', get_guess)
