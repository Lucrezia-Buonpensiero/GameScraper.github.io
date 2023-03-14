from whoosh.fields import SchemaClass, TEXT, ID


class IndexScheme(SchemaClass):
    url = ID(stored=True)
    nome_gioco = TEXT(phrase=True, stored=True)
    console = TEXT(phrase=True, stored=True)
    voto = TEXT(phrase=True, stored=True)
    data = TEXT(phrase=True, stored=True)
    genere = TEXT(phrase=True, stored=True)
    descrizione = TEXT(phrase=True, stored=True)

