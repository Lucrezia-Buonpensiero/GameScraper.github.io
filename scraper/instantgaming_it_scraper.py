import csv
import json


class InstantGamingScraper():
    def scrape(self):
        with open("csv-files/instantgaming.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # per skippare la prima riga del file csv ("nome", "console"...)
            data = {"giochi": []}

            for row in reader:
                data["giochi"].append({
                    "url": row[3],
                    "nome_gioco": row[4],
                    "console": row[8],
                    "voto":row[6],
                    "data": row[7],
                    "genere": row[5],
                    "descrizione": row[9],
                })
        with open("./scraper/json-files/instant-gaming.json", "w") as f:
            json.dump(data, f, indent=4)

        print("instant-gaming scraping completed")
