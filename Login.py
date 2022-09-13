import requests
from bs4 import BeautifulSoup

class ExcecaoHTTP(Exception):
    def __init__(self):
        self.msg = "Credenciais inválidas. Favor tentar novamente."
        super().__init__(self.msg)
try:
    url = "https://www.scrapethissite.com/pages/advanced/?gotcha=csrf"
    login = input("Login: ")
    senha = input("Senha: ")
    obj = {'user': login, 'pass': senha, 'csrf': '510618827'}
    response = requests.post(url, data = obj)
    soup_instance = BeautifulSoup(response.content, 'html.parser')
    busca_erro = soup_instance.find(attrs={'class': 'error alert alert-danger'})
    if busca_erro is not None:
        raise ExcecaoHTTP
    menu_items = soup_instance.find('div', attrs={'class': 'col-md-4 col-md-offset-4'})
    print(menu_items.text)
except ExcecaoHTTP as erro:
    print(erro)
