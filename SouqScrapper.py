from ShopScrapper import ShopScrapper


class SouqScrapper(ShopScrapper):

    HEADERS = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/78.0.3904.108 Safari/537.36 "
    }

    url = 'https://egypt.souq.com/eg-en/{item}/s/?as=1'

    def __init__(self, item_name: str):
        super().__init__(item_name)

    def fetchProducts(self, soup: str) -> list:
        products = soup.find_all('div', class_='single-item')
        result = []
        for product in products:
            titleDIV = product.find_all('h6', class_='title itemTitle')
            price = product.find_all('span', class_='itemPrice')
            image = product.find_all('img', class_='img-size-medium')[0]['src']
            result.append({
                "name": titleDIV[0].text.replace('\n', '').strip(),
                "link": titleDIV[0].findChildren('a', recursive=False)[0]['href'],
                "price": price[0].text,
                "image": image
            })

        return result
