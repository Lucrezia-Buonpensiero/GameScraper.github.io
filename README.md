ProgettoGestione_Arseni-Buonpensiero


### *Sviluppatori*
Arseni Giulia (Matr: 123121) <br />
Buonpensiero Lucrezia (Matr: 110796)

___



# ***GameScraper***

GameScraper è un search engine ideato per effettuare la ricerca di videogiochi sviluppato utilizzando il linguaggio python con l'ausilio della libreria Whoosh, bootstrap, jquery, Flask. <br/>
Questo search engine permette di effettuare la ricerca di titoli videoludici da diverse fonti in base alle query immesse dall'utente nella barra di ricerca.

Con il dropdown menù di fianco alla barra di ricerca è possibile selezionare il criterio di ricerca in base a:
* nome;
* console;
* voto;
* genere;
* data di uscita;
* descrizione;


L'index viene generato in formato CSV a partire da un dump fornito da:
* Multiplayer.it
* Everyeye.it
* InstantGaming.it

Il CSV viene trasformato in un .json tramite la libreria json e le rispettive funzioni all'interno della cartella _scraper_.

---

## Ranking
Viene calcolato il pagerank per ogni articolo per facilitare la visualizzazione e l'ordinamento degli articoli più pertinenti.

___

## Tokenizzazione e Parsing
Durante la fase di preprocessing viene effettuato sul testo cercato dall'utente la Tokenizzazione e il Parsing che rispettivamente consentono di "sfoltire" il testo per facilitare il match delle query.
Il testo ripulito verrà inserito nell'index.

---

## Queries

Le queries per i benchmark sono:

1. quando è uscito dark souls 3? </br>
```nome_gioco:"dark souls 3" AND data```

2. data di sucita di resident evil 2 *MA SBAGLIANDO LA QUERY DI PROPOSITO* </br>
```nome_gioco:"resident evillq 2" AND data```

3. giochi di ruolo usciti nel 2020 </br>
```data:2020 AND genere:"gioco di ruolo"```

4. giochi usciti nel 2015 </br>
```data:2015```

5. giochi usciti dal 2015 al 2017 ordinati per ordine più recente di uscita che abbiano nel nome la parola "god" </br>
```(data:2015 OR data:2016^2 OR data:2017^4) AND (nome_gioco:god)```

6. god of war c'è per ps4? </br>
```nome_gioco:"god of war" and console:ps4```

7. data di uscita di lost planet 2 </br>
```nome_gioco:"lost planet 2" AND data```

8. mi consigliate un gioco sparatutto? </br>
```(genere:sparatutto OR genere:fps) AND (voto:9 OR voto:10^2)```

9. miglior gioco del 2022 </br>
```data:2022 AND (voto:10)```

10. giochi in uscita a maggio 2022 </br>
```data:"maggio 2022"```

___
## Risultati

I risultati della ricerca saranno tutti i titoli corrispondenti ai criteri di ricerca con specificato il TITOLO, la DATA, 
le CONSOLE su cui è supportato il gioco e la SORGENTE da cui è stato rilevato il documento.

---
## *Caratteristiche*

Abbiamo implementato una semplice interfaccia web utilizzando Flask in cui è presente una barra
di ricerca in cui è possibile inserire una parola o una frase in base alla quale verranno
restituiti diversi risultati. <br/>
I risultati sono cliccabili, di fatto, l'utente verrà indirizzato alla pagina da cui
è stato fatto lo scraping.<br/>
Se, rispetto ad una frase inserita, non vengono generati risultati, l'interfaccia si occuperà
di comunicarlo all'utente.
---

## *Avvio*
Il progetto si compone di 4 fasi:
1. Viene effettuata la traduzione in json del risultato dello scraping dei siti web presente all'interno del file CSV.
2. Entriamo nella fase di preprocessing, in cui viene analizzato il testo e indicizzato, in questa fase viene creato l'index.
3. La GUI viene inizializzata e avviata, permettendo all'utente di cercare quello di cui ha bisogno.
4. OPZIONALE: può essere avviata la fase di benchmark per il calcolo dell'Average Precision e Mean Average Precision

Nella Root Folder del progetto possiamo avviare GameScraper e la sua relativa GUI da terminale attraverso il comando:

```
python3 main.py
```
Dopodiché posso decidere di effettuare l'indexing:
verrà chiesto: "*vuoi ricreare l'indexing?* " <br />
Premendo il tasto _**Y**_ l'indexing verrà ricreato, altrimenti, premendo _**N**_ non verrà ricreato. <br />
Infine apparirà l'indirizzo **127.0.0.1/5000** , cliccando sul quale si verrà reindirizzati alla pagina web contenente l'home page
di GameScraper.


---

## *Requirements*
Se necessario, prima dell'avvio, installare i pacchetti presenti in _**requirements.txt**_
tramite il comando
```
pip install -r requirements.txt
```

---

## Come effettuare i Test
Per effettuare i test, bisogna far partire singolarmente il file ```test_efficienza_dati.py``` che si trova all'interno
della cartella _benchmark_.
Verrà stampata a schermo la AVERAGE PRECISION e la MEAN AVERAGE PRECISION calcolata.

Inoltre è possibile generare un grafico relativo alle precision:
E' sufficiente far partire il file ```graph_test.py``` e come risultato si otterrà un grafico delle prestazioni
all'interno del percorso _/benchmark/plot-data_.

___

## Struttura Cartelle del Progetto

In ordine alfabetico:
- **/benchmark**: Contiene quanto necessario per effettuare i Test e include:  </br> **/json-data-test** contiene il file json del modello BM25F. </br> **/plot-data** contiene il grafico dell'AP e il valore del MAP. </br>
- **/csv-files**: contiene i file CSV delle pagine web di cui è stato effettuato lo scraping.
- **/index**: contiene i file con gli index.
- **/scheme**: contiene le funzionalità per la fase di preprocessing e per effettuare la ricerca.
- **/scraper**: Contiene le funzionalità che convertono i file CSV in json e li memorizzano nella sottocartella **/json-files**.
- **/web**: E' contenuta la GUI e le funzionalità per il suo avvio.
- **main.py** : Permette l'avvio del progetto richiamando le funzioni di base.

---

## Note Finali
* Per creare il file *requirements.txt* lanciare il seguente comando da terminale: ```pip3 freeze > requirements.txt``` 

* Se vogliamo cercare un videogioco per query che abbia come caratteristica, ad esempio, 
voto _"Non Classificato"_ basta inserire nella barra di ricerca 
```voto:null``` <br/>
Stessa cosa per gli altri campi.
* Se vogliamo mostrare i ranking, decommentiamo la riga 54 nel file searching.py

----