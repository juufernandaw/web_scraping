import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
filmes = soup.find_all("td", {"class": ["ratingColumn imdbRating", "titleColumn"]})

i = 0
elencos = []
lancamentos = []
nomes = []
avaliacoes = []

while i < len(filmes):
    elenco = filmes[i].a['title']
    nome = filmes[i].a.text
    lancamento = (filmes[i].span.text).strip('()')
    avaliacao = filmes[i+1].strong.text
    elencos.append(elenco)
    nomes.append(nome)
    lancamentos.append(lancamento)
    avaliacoes.append(avaliacao)
    i += 2

base = pd.DataFrame()
base['Nome'] = nomes
base['Ano'] = lancamentos
base['Elenco'] = elencos
base['Avaliacao'] = avaliacoes

base.to_csv("ranking_melhores_filmes.csv", index=False, header=True)
