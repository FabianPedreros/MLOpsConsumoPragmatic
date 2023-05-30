import wikipedia
from textblob import TextBlob 


def wiki(name="War Goddess", lenght=1):
    """This is a wikipedia fetcher"""
    my_wiki = wikipedia.summary(name, lenght)
    return my_wiki


def search_wiki(name):
    """Buscar en Wikipedia nombres"""
    results = wikipedia.search(name)
    return results

def phrase(name):
    """Revuelve frases de wikipedia"""
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
