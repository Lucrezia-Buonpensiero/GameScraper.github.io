import csv
import json


class MultiplayerItScraper():

    
    def scrape(self):
        with open("csv-files/multiplayer.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # per skippare la prima riga del file csv ("nome", "console"...)
            data = {"giochi": []}

            for row in reader:

                data["giochi"].append({
                    "url": row[3],
                    "nome_gioco": row[4],
                    "console": row[7],
                    "voto": row[5],
                    "data": row[6],
                    "genere": row[8],
                    "descrizione": row[9],
                })
        with open("./scraper/json-files/multiplayer-it.json", "w") as f:
            json.dump(data, f, indent=4)

        print("multiplayer scraping completed")
