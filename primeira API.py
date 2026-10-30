import requests

resposta = requests.get("https://jsonplaceholder.typicode.com/users")

dados = resposta.json()

for dado in dados:
    print(dado["name"])