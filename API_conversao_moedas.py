import requests

url = "https://www.google.com"
response = requests.get(url)

response.content

#json
myjson = {"Julia":20, "Paula":26}

currency = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(currency)

data = response.json()

data

data['rates']

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
moeda_usd = response.json()
moeda = input("Digite a sua moeda")
qtd = input("Digite a sua qtd da moeda")
print(moeda_usd['rates'][moeda])
resultado = (float(moeda_usd['rates']['USD']))*int(qtd)/float(moeda_usd['rates'][moeda])
print("O resultado em euros para a moeda {} é: ".format(moeda), resultado)
