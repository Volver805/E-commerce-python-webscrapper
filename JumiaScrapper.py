from ShopScrapper import ShopScrapper


class JumiaScrapper(ShopScrapper):

    HEADERS = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/78.0.3904.108 Safari/537.36 "
    }

    BASEURL = 'https://www.jumia.com.eg'

    url = 'https://www.jumia.com.eg/catalog/?q={item}'

    def __init__(self, item_name: str):
        super().__init__(item_name)

    def fetchProducts(self, soup: str) -> list:
        products = soup.select('article.prd:not(.dis)')
        result = []
        for product in products:
            if '_dis' not in product['class']:
                name = product.find_all('h3', class_='name')
                price = product.find_all('div', class_='prc')
                image = product.find_all('img', class_='img')[0]['src']
                link = product.find_all('a', class_='core')
                result.append({
                    "name": name[0].text,
                    "link": self.BASEURL + link[0]['href'],
                    "price": price[0].text.replace('EGP', ''),
                    "image": image
                })

        return result
