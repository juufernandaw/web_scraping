import requests
from bs4 import BeautifulSoup
import json

# 1) Entre no site WebScraper Test e imprima todos os títulos e preços dos laptops disponíveis. Esse site possui
# paginação AJAX, você deve iterar todas as páginas e pegar a informação pedida de todos os itens.
url = "https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"
response = requests.get(url)
soup_instance = BeautifulSoup(response.content, 'html.parser')
menu_items = soup_instance.find('div', attrs={'class': 'row ecomerce-items ecomerce-items-ajax'})
lista = list(eval(menu_items['data-items'])) # executa códigos em python dentro de uma string. eval() avalia se é um
# comando valido do python
for item in lista:
    print("Título: ", item['title'], " Preço: ", item['price'])
