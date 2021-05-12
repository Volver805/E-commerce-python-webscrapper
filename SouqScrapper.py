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
            image = product.find_all('img', class_='img-size-medium')[0]
            if image.has_attr('data-src'):
                image = image['data-src']
            else:
                image = image['src']
            result.append({
                "name": product.select('.itemTitle')[0].text.replace('\n', '').strip(),
                "link": product.select('.itemLink ')[0]['href'],
                "price": product.select('.itemPrice')[0].text,
                "image": image
            })

        return result
