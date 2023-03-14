from urllib.parse import urlparse
from scheme.manager_scheme import ManagerScheme
from scheme.searching import Searching


def get_ajax_results(field, query):
    out = ''

    fields = {
        'Nome': 'nome_gioco',
        'Console': 'console',
        'Voto': 'voto',
        'Data di uscita': 'data',
        'Genere': 'genere',
        'Descrizione': 'descrizione',
        'Cerca': 'descrizione',
    }

    searcher = Searching(ManagerScheme('index'))
    ranking = searcher.search_in_field(fields[field], query)


    if ranking == 1:                                            # se il ranking della funzione chiamata è 1
        return '<h5 class="text-center">Nessun Risultato</h5>'  # (ho messo la condizione nella funzione search_in_field)
                                                                # allora mi dice che non ho risultati.
    if not searcher.empty_ranks(ranking):
        for i in range(min(10, len(ranking))):
            rank = ranking[i][1]

            domain = urlparse(rank['url']).netloc
            name_domain = ''
            if domain == 'multiplayer.it':
                name_domain = 'Multiplayer'
            elif domain == 'www.everyeye.it':
               name_domain = 'Everyeye'
            elif domain == 'www.instant-gaming.com':
               name_domain = 'InstantGaming'

            if rank['data'] == 'null':
                rank['data'] = 'Nessuna data disponibile'
            if rank['voto'] == 'null':
                rank['voto'] = 'Non Classificato'
            if rank['console'] == 'null':
                rank['console'] = "Per questo gioco non sono disponibili console"

            out +=  '<blockquote class="blockquote">' + \
                        '<div class="row">' + \
                            '<div class="col-12 col-md-9">' + \
                                '<a href="' + rank['url'] + '" target="_blank"><h4 class="mb-0">' + rank['nome_gioco'] + '</h4></a>' + \
                                '<h6 class="mb-0">' + rank['console'] + ([' - ', ''][rank['console'] == '' or rank['voto'] == '']) + rank['voto'] + '</h6>' + rank['data'] + \
                                '<footer class="blockquote-footer">Sorgente: <cite title="Source Title">' + name_domain + '</cite></footer>' + \
                            '</div>'


            out += '</div>' + \
                   '</blockquote>'

        return out