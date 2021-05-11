from ShopScrapper import ShopScrapper


class NoonScrapper(ShopScrapper):

    HEADERS = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/78.0.3904.108 Safari/537.36 "
    }

    BASEURL = 'https://www.noon.com'

    url = 'https://www.noon.com/egypt-en/search?q={item}'

    def __init__(self, item_name: str):
        super().__init__(item_name)

    def fetchProducts(self, soup: str) -> list:
        products = soup.select('div.productContainer')
        result = []
        for product in products:
            result.append({
                'name': product.find(attrs={'data-qa': 'product-name'}).text,
                'price': product.find(attrs={'data-qa': 'productPrice'}).text,
                'link': self.BASEURL + product.find('a')['href'],
                'image': None
            })

        return result


