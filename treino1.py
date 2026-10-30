import requests

# Use https://jsonplaceholder.typicode.com/users.
# Mostre apenas os usuários que:
# - Moram em Gwenborough.
# - Têm um nome que contém a letra a.

url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url)

dados = resposta.json()

for dado in dados:
    if dado["address"]["city"] == "Gwenborough":
        if "u" in dado["name"]:
            print(dado["name"])
else:
    print("Não tem ninguem com esse nome")