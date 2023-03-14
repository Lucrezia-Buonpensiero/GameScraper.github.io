from statistics import mean
from time import time
from json import dump
from scheme.manager_scheme import ManagerScheme
from scheme.searching import Searching
from eldar import Query


def averageP(queries):
    data = {'queries': []}
    searcher = Searching(ManagerScheme('../index')) #va a cercre nel'index creato
    relevant_res = []
    count = 0
    rel = 0
    precision = []
    AP = []


    for query in queries:
        start_time = int(round(time() * 1000))
        result = searcher.search_in_field('descrizione', query[0]) #sostituire con descrizione
        stop_time = int(round(time() * 1000))

        if result == 1:
            return print("no data")
        result_sliced = result[:10]

        # ho creato un array contenenti i documenti importanti, assunto che essi abbiano rank >= 16
        for x in range(len(result_sliced)):
            #print(result_sliced[x][0])
            if result_sliced[x][0] >= 16:
                #print(result_sliced[x][0])
                relevant_res.append(result_sliced[x])


        # ora, per tutti i titoli, creo un contatore. SE il titolo matcha il relevant_res, allora
        # vado ad aumentare il rel: vedi formula pag 50.
        for title in result_sliced:
            count += 1              # quanti cercati
            if title in relevant_res:
                #print(title)
                rel += 1            # quanti trovati
                precision.append(round(rel/count, 2))

        if len(relevant_res) != 0:
            AP.append(round(sum(precision)/count, 2))   #average precision per un certo lvl di recsll
        else:
            AP.append(0)

        data['queries'].append({
            'query': query[0],
            'time': stop_time - start_time,
            'A': min(10, len(result)),
            'precision' : round(rel/count, 2), #vedere se va modificata
        })


    print(" ")
    print(" ------------------------ ")
    print(" ------ EVALUATION ------ ")
    print(" ------------------------ ")
    print("Average Precision", AP)
    print("Mean Average Precision", round(mean(AP), 2))
    data['averagePrec'] = AP #questo è il risultato della average precision
    return data

def save_json_data(file, data):
    with open(file, 'w') as outfile:
        dump(data, outfile, indent=4)


if __name__ == '__main__':
    queries = [
        # Da aggiungere le query per i test
        ['nome_gioco:"dark souls 3" AND data'],
        ['nome_gioco:"resident evillq 2" AND data'],
        ['data:2020 AND genere:"gioco di ruolo"'],
        ['data:2015'],
        ['(data:2015 OR data:2016^2 OR data:2017^4) AND (nome_gioco:god)'],
        ['nome_gioco:"god of war" and console:ps4'],
        ['nome_gioco:"lost planet 2" AND data'],
        ['(genere:sparatutto OR genere:fps) AND (voto:9 OR voto:10^2)'],
        ['data:2022 AND (voto:10)'],
        ['data:"maggio 2022"'],
    ]
    file_name = 'json-data-test/BM25F.json'

    data = averageP(queries)
    save_json_data(file_name, data)
