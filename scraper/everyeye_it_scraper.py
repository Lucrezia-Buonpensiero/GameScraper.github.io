import csv
import json


class EveryeyeScraper():
    def scrape(self):
        with open("csv-files/everyeye.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # per skippare la prima riga del file csv ("nome", "console"...)
            data = {"giochi": []}
            for row in reader:
                data["giochi"].append({
                    "url": row[9],
                    "nome_gioco": row[10],
                    "console": row[11],
                    "voto": row[12],
                    "data": row[13],
                    "genere": row[14],
                    "descrizione": row[15],
                })
        with open("./scraper/json-files/everyeye-it.json", "w") as f:
            json.dump(data, f, indent=4)

        print("everyeye scraping completed")

