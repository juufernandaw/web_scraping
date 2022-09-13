#3) Entre no site Scrape this site e imprima a mensagem principal no body da página. Para conseguir realizar a requisição da página,
#você deve trabalhar com headers. Entenda como seu navegador faz a chamada da página, os headers utilizados e reproduza.

import requests
from bs4 import BeautifulSoup

url = "http://www.scrapethissite.com/pages/advanced/?gotcha=headers"
header = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.878675421.1662136258; _gcl_au=1.1.190796872.1662136258; _gid=GA1.2.2039834370.1662333694; _gat=1',
        'Host': 'www.scrapethissite.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
         }
response = requests.post(url, headers = header)
print(response)
soup_instance = BeautifulSoup(response.content, 'html.parser')
menu_items = soup_instance.find('div', attrs={'class': 'col-md-4 col-md-offset-4'})
print(menu_items.text)
