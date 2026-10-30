import requests

# Busque os posts em:
# https://jsonplaceholder.typicode.com/posts
# Mostre apenas os posts do usuário de ID 3.

url = "https://jsonplaceholder.typicode.com/users/3/posts"
resposta = requests.get(url)

dados = resposta.json()

for dado in dados:
    print(dado["userId"])