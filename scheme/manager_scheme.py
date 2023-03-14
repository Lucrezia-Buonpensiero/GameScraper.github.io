from os import path, mkdir
from json import load

from whoosh.filedb.filestore import FileStorage
from whoosh.qparser import QueryParser
from scheme.index_scheme import IndexScheme
from whoosh.scoring import BM25F


class ManagerScheme:
    def __init__(self, dir_name):
        self.dir_name = dir_name
        self.storage = FileStorage(self.dir_name)
        self.ix = None
        self.thesaurus = None

    def create_index_scheme(self):
        # create directory if not exists
        if not path.exists(self.dir_name):
            mkdir(self.dir_name)

        # create index from scheme
        self.ix = self.storage.create_index(IndexScheme(), indexname="usages")

    def open_scheme(self):
        if self.ix is None:
            # load index
            self.ix = self.storage.open_index(indexname="usages")

    def add_json_to_scheme(self, json_file_name, root_object):
        # open index
        self.open_scheme()

        # add documents to index
        writer = self.ix.writer()
        with open(json_file_name) as json_file:
            data = load(json_file)
            for elem in data[root_object]:
                writer.add_document(
                    url=elem['url'],
                    nome_gioco=elem['nome_gioco'],
                    console=elem['console'],
                    voto=elem['voto'],
                    data=elem['data'],
                    genere=elem['genere'],
                    descrizione=elem['descrizione'],
                )
        writer.commit(optimize=True)

    def search_into_scheme(self, field, search_text):

        def hit_to_dict(hit):
            return {
                'url': hit['url'],
                'nome_gioco': hit['nome_gioco'],
                'console': hit['console'],
                'voto': hit['voto'],
                'data': hit['data'],
                'genere': hit['genere'],
                'score': hit.score,
                'descrizione': hit['descrizione']
            }

        # open index
        self.open_scheme()

        dict_results = []

        #modello BM25F
        with self.ix.searcher(weighting=BM25F()) as s:
            q = QueryParser(field, schema=self.ix.schema).parse(search_text)
            print(" ")
            print(" --------------------- ")

            print(search_text, "<-- testo che inserisco")
            print(q, "<-- viene trasformata la richiesta in query")
            #___CORREZIONE ERRORI BATTITURA______________________

            corrected = s.correct_query(q, search_text)

            if corrected.query != q:
                print("Did you mean:", corrected.string, "instead of ", search_text)          # stampa di controllo, poi la si toglie
                q = QueryParser(field, schema=self.ix.schema).parse(corrected.string)         # se la stringa è corretta, allora                                                                           # effettua nuovamente il parsing ma
                                                                                              # stavolta con la stringa corretta
            #______________________________________________________

            results = s.search(
                q,
                limit=None
            )

            for i in range(0, len(results)):
                dict_results.append(hit_to_dict(results[i]))

            if not dict_results:
                print("non sono presenti risultati")

        return dict_results
