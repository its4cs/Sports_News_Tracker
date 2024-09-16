from sportscraper.spiders.gamescraper import GamescraperSpider
from datetime import datetime
class Footballscrapper(GamescraperSpider):
    game_name = "football"
    name = game_name + "scraper"
    def __init__(self):
        
        super().__init__()
        self.set_name()
    
    def set_name(self):
        self.start_urls = [
            f"https://www.espn.in/{self.game_name}/scoreboard"+"/_/date/"+datetime.now().strftime('%Y%m%d'),
            # f"https://www.espn.in/{self.game_name}/scoreboard"+"/_/date/"+"20240915"
            ]
        