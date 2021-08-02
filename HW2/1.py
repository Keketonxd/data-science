from bs4 import BeautifulSoup as bs
import requests
import json
import os
import traceback

url = 'https://roscontrol.com'
main_url_adder = '/category/produkti'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36"}
response_main = requests.get(url + main_url_adder + '/#popup', headers=headers)
soup_main = bs(response_main.text, 'html.parser')
products_list = soup_main.find_all('div', attrs={
                                   'class': 'grid-padding grid-column-3 grid-column-large-6 grid-flex-mobile grid-column-middle-6 grid-column-small-12 grid-left'})

products = []
categories = []
finals = []

for product in products_list:
    this_product = product.find('a').get('href')[19:-1]
    products.append(this_product)
    print(this_product)

arg1 = input('Это категории продуктов, выберите одну из них: ')


if arg1 in products:
    response_1 = requests.get(url + main_url_adder + '/' + arg1 + '/')
    soup_1 = bs(response_1.text, 'html.parser')
    categories_list = soup_1.find_all('div', attrs={
        'class': 'grid-padding grid-column-3 grid-column-large-6 grid-flex-mobile grid-column-middle-6 grid-column-small-12 grid-left'})
    for category in categories_list:
        this_category = category.find('a').get('href')[20 + len(arg1):-1]
        categories.append(this_category)
        print(this_category)
    arg2 = input(
        'Это категории категорий продуктов :), выберите одну из них: ')

    if arg2 in categories:
        response_2 = requests.get(
            url + main_url_adder + '/' + arg1 + '/' + arg2 + '/')
        soup_2 = bs(response_2.text, 'html.parser')
        final_list = soup_2.find_all('div', attrs={
            'class': 'wrap-product-catalog__item grid-padding grid-column-4 grid-column-large-6 grid-column-middle-12 grid-column-small-12 grid-left js-product__item'})
        for final in final_list:
            final_link = final.find('a').get('href')
            response_final = requests.get(
                url + final_link)
            soup_final = bs(response_final.text, 'html.parser')

            if soup_final.find(
                    'div', attrs={'class': 'product__single-subtitle'}).getText() == 'Общая оценка':
                name = soup_final.find(
                    'h1', attrs={'class': 'main-title testlab-caption-products util-inline-block'}).getText()
                rating = int(soup_final.find(
                    'div', attrs={'class': ['total green', 'total orange', 'total red']}).getText())
                qualities = soup_final.find_all(
                    'div', attrs={'class': 'rate-item__value'})
                try:
                    safety = int(qualities[0].getText().replace(
                        '\n', '').replace('\\n', ''))
                    naturality = int(qualities[1].getText().replace(
                        '\n', '').replace('\\n', ''))
                    nutrition = int(qualities[2].getText().replace(
                        '\n', '').replace('\\n', ''))
                    quality = int(qualities[3].getText().replace(
                        '\n', '').replace('\\n', ''))
                except Exception:
                    safety = None
                    naturality = None
                    nutrition = None
                    quality = None
                site = url + final_link
                product_info = {
                    'name': name,
                    'rating': rating,
                    'safety': safety,
                    'naturality': naturality,
                    'nutrition': nutrition,
                    'quality': quality,
                    'site': site
                }
                print(product_info)
                finals.append(product_info)
            print(finals)
            with open('HW2/1.json', 'w', encoding='utf-8') as f:
                json.dump(str(finals), f, ensure_ascii=False)
