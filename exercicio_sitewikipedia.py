import requests
from bs4 import BeautifulSoup

site = "https://en.wikipedia.org/wiki/Music"
response = requests.get(site)
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

links = soup.findAll('a')
lista = [item.string for item in links if item.string is not None]
# print(lista) #lista com o texto dos links
# print(item.get('href')) #mostra todos os links dentro de href
# print(item.string) #mostra os textos dentro da tag a

h2 = soup.findAll('h2')
h2_lista = [item.string for item in h2 if item.string is not None]
# print(h2_lista)

footer = soup.find('footer')
# print(footer.text)
