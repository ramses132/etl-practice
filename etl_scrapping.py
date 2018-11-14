import bonobo
import requests
from bs4 import BeautifulSoup


def scrape_amazon_laptops():
    title_div = {
        'class': 'a-section a-spacing-none acs-showcase-product-title'
    }
    product_div = {'class': 'a-fixed-left-grid-col a-col-right'}
    product_show_div = {
        'class': 'a-section a-spacing-none s-result-card acs-showcase-card'
    }
    product_fixed_div = {'class': 'a-fixed-left-grid-inner'}
    price_div = {'class': 'sx-price sx-price-large'}

    url = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=laptop+gaming'
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        html = res.text.strip()
        soup = BeautifulSoup(html, 'html.parser')
        soup.find_all(attrs=product_div)
    
        for div in soup.find_all(attrs=product_div):
            
            title = div.find(
                attrs={
                    'class':
                    'a-row a-spacing-none scx-truncate-medium sx-line-clamp-2'
                })
            if not title:
                continue
            title = title.a.text
            price = div.find(attrs='sx-price-whole')
            if not price:
                continue
            price = price.text
            product = (title, price)
            yield product
        """
        + soup.find_all(
            attrs=product_show_div) + soup.find_all(attrs=product_fixed_div)
        """
        #yield ('', '')


def extract():
    return scrape_amazon_laptops()


def transform(*product: tuple):

    yield "{} - {}".format(product[0].upper(),
                           product[1].replace(',', '').lstrip('$'))


def load(*product: str):

    f = open('amazon_laptops.txt', 'a+', encoding='utf8')
    for p in product:
        f.write((str(p) + '\n'))
    f.close()


if __name__ == "__main__":
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/39.0.2171.95 Safari/537.36'
    }

    graph = bonobo.Graph(
        extract,
        transform,
        load,
    )
    bonobo.run(graph)
