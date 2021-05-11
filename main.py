from SouqScrapper import SouqScrapper
from JumiaScrapper import JumiaScrapper
from NoonScrapper import NoonScrapper


def search_product(productName: str) -> dict:
    return {
        "jumia_products": JumiaScrapper(productName).scrape(),
        "souq_products": SouqScrapper(productName).scrape(),
        "noon_products": NoonScrapper(productName).scrape()
    }


products = search_product('logitech g29')

