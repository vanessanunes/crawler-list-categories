import requests
from bs4 import BeautifulSoup
from pprint import pprint

class CrawlerBasic:
    def __init__(self):
        print('hello, start get categories from menu of Magazine Luiza web store')
    
    def _get_html(self):
        site = 'https://www.magazineluiza.com.br/'
        req = requests.get(site)
        html = req.content
        return BeautifulSoup(html, 'html.parser')

    def _get_items(self, code):
        menu = code.find('div', {'class', 'position-menus'}).find_all('li')
        get_menus = []

        for item in menu:
            if item.find('a') is None:
                pass
            else:
                get_menus.append(
                    {
                        'nome': item.find('a').text,
                        'link': item.find('a')['href']
                    }
                )

        return get_menus

    def get_categories(self):
        code = self._get_html()
        items = self._get_items(code)
        categories = {'categories': items}
        return categories

if __name__ == '__main__':
    pprint(CrawlerBasic().get_categories())
    