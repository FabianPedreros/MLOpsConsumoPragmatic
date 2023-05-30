import wikipedia


def wiki(name="War Goddess", lenght=1):
    """This is a wikipedia fetcher"""
    my_wiki = wikipedia.summary(name, lenght)
    return my_wiki

def search_wiki(name): 
    """Buscar en Wikipedia nombres"""
    results = wikipedia.search(name)
    return results