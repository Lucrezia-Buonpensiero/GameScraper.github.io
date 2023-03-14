import whoosh.spelling
from nltk.corpus import wordnet as wn
from whoosh.analysis import RegexTokenizer, LowercaseFilter


class Searching:

    def __init__(self, manager_scheme):
        self.manager_scheme = manager_scheme


    def search_in_field(self, field, phase):
        rankings = []
        terms = self.__analyze_phase(phase)         #chiama la funzione di sotto che "separa" tutti i termini

        ricerca = self.__search(field, ' '.join(terms))
        if ricerca != 0:
            rankings.append(ricerca)
        else:
            return 1                                # se tutto è andato bene, viene fatto l'append ai ranking
                                                    # altrimenti ritorna 1 (errore) in fun.


        if self.empty_ranks(rankings):
            # alla fine chiama merge_ranks che effettua ranking
            synonyms_array = self.__get_synonyms_from_token_list(terms)

            for key, ins in synonyms_array.items():
                for term in ins:
                    temp_temp = terms[key]
                    terms[key] = term
                    phase = ' '.join(terms)
                    terms[key] = temp_temp
                    rankings.append(self.__search(field, phase))
        return self.__merge_ranks(rankings)

    def __search(self, field, phase):
        ranking = {}

        i = 0
        dictionary = self.manager_scheme.search_into_scheme(field, phase)
        #data una certa query (phase) mi va a cercare tutti i giochi relativi a quella quey presenti
        #nello schema.

        # se non trova niente nel dizionario... ritorna che nei ranking ci appende 0.
        if not dictionary:
            return 0            # se qui ho messo 0, non è true, è per indicare che il rank lo metto a 0
                                # visto che sotto, la funzione ritorna il ranking

        for result in dictionary:
            score = result['score']
            del result['score']
            ranking[i] = [score, result]
            #print(score)          # <-- DECOMMENTA PER MOSTRARE IL RANKING
            i += 1
        return ranking

    @staticmethod
    def empty_ranks(ranks):
        for rank in ranks:
            if rank:
                return False
        return True

    @staticmethod
    def __merge_ranks(ranks):
        ranking = []
        for rank in ranks:
            for rank_item in rank.values():
                found = False
                for key, ranking_item in enumerate(ranking):
                    if ranking_item[1] == rank_item[1]:
                        ranking[key][0] += rank_item[0]
                        found = True
                if not found:
                    ranking.append(rank_item)

        return sorted(ranking, key=lambda x: x[0], reverse=True)

    ### Funzione che effettua la divisione dei singoli termini
    @staticmethod
    def __analyze_phase(phase):
        buffer = ''
        struct = []
        for c in phase:
            if c == ' ' or c == '(' or c == ')':
                if buffer != '':
                    struct.append(buffer)
                    buffer = ''
                if c != ' ':
                    struct.append(c)
            else:
                buffer += c
        if buffer != '':
            struct.append(buffer)

        #### ANALYZER CUSTOMIZZATO PER TOKEN, STOPFILTER E LOWERCASE ############
        my_analyzer = RegexTokenizer() | LowercaseFilter() | whoosh.analysis.StopFilter(stoplist=['is', 'to', 'of'])

        temp_query = []
        for token in my_analyzer(phase):
            temp_query.append(token.text)
        #########################################################################
        return struct


    #lemmatizzazione
    @staticmethod
    def __get_synonyms_from_token_list(terms):
        words = {}
        white_list = ['to', 'not', 'and', 'or', 'TO', 'NOT', 'AND', 'OR', '(', ')']
        wildcard_word = '*'
        wildcard_char = '?'

        for i in range(len(terms)):
            term = terms[i]

            if term not in white_list \
                    and wildcard_word not in term \
                    and wildcard_char not in term:

                ins = set()

                for syn in wn.synsets(term, lang='ita'):
                    ins = ins.union({e.name().replace('_', ' ') for e in syn.lemmas(lang='ita')})

                if term in ins:
                    ins.remove(term)

                words[i] = ins
        return words
