import requests
from bs4 import BeautifulSoup


class ShopScrapper:

    def __init__(self, item_name: str):
        self.item = item_name

    def scrape(self) -> list:
        self.url = self.url.replace('{item}', self.item)
        request = requests.get(self.url, headers=self.HEADERS)
        soup = BeautifulSoup(request.content, 'lxml')
        return self.fetchProducts(soup)

    def fetchProducts(self, soup: str) -> list:
        pass
