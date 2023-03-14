from scheme.manager_scheme import ManagerScheme
from scraper.everyeye_it_scraper import EveryeyeScraper
from scraper.instantgaming_it_scraper import InstantGamingScraper
from scraper.multiplayer_it_scraper import MultiplayerItScraper
from web.web import website


def create_index(json_directory, web_scraper):
    manager = ManagerScheme('index')
    manager.create_index_scheme()

    for web in web_scraper.keys():
        print('. ')
        manager.add_json_to_scheme(json_directory + web + '.json', 'giochi')

    print("done")

if __name__ == '__main__':
    json_directory = 'scraper/json-files/'

    MultiplayerItScraper.scrape(self=1),
    EveryeyeScraper.scrape(self=1),
    InstantGamingScraper.scrape(self=1)

    web_scraper = {
        'multiplayer-it': [MultiplayerItScraper(), 5],  # max-page 2
        'instant-gaming' : [InstantGamingScraper() , 5],
        'everyeye-it' : [EveryeyeScraper(), 5]
    }

    scelta = input('vuoi ricreare l\'index? Y-YES N-NO')

    if scelta == 'Y' or scelta == 'y':
        create_index(json_directory, web_scraper)
    website()
