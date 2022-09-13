import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud
import string
from urllib.request import urlopen
from bs4 import BeautifulSoup
nltk.download('punkt')

html = urlopen("https://g1.globo.com/economia/noticia/2022/09/01/petrobras-anuncia-nova-reducao-no-preco-da-gasolina.ghtml")
res = BeautifulSoup(html.read(),"html.parser")
#print(res.title)
#tags = res.findAll("h3", {"class": "pt-cast-title"})
tags = res.findAll("p") #busca todo o conteúdo das tags <p>
txt = ""
for tag in tags:
    txt += tag.getText() #pega somente o texto das tags
txt_min = txt.lower()
txt_sem_pontuacao = ''.join([t for t in txt_min if t not in string.punctuation and t.isnumeric()==False]) #retirar pontuação
tokenizacao = nltk.word_tokenize(txt_sem_pontuacao) #separando palavra por palavra

#nltk.download('stopwords')
stopwords = stopwords.words('portuguese')
palavras_sem_stop = [p for p in tokenizacao if p not in stopwords and len(p)>1] #retirando as stopwords

tokenizacao_str = ' '.join([y for y in palavras_sem_stop if len(y)>1]) #transforma a lista em string pq o wordcloud.generate() espera uma string
frequencia = FreqDist(palavras_sem_stop) #conta a qtd de ocorrencias de cada palavra
frequencia = frequencia.most_common(8)

nuvem_palavras = WordCloud(
                    background_color = 'white',
                    stopwords = stopwords,
                    width = 1000,
                    height = 1000,
                    max_words = 25
)
nuvem_palavras.generate(tokenizacao_str) #gera a wordcloud
nuvem_palavras.to_file('nuvem.png') #salva em um arquivo 
