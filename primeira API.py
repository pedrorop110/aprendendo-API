import requests

# GET = Significa fazer um pedido para um servidor para buscar, consultar ou ler dados, sem alterar nenhuma informação lá dentro

resposta = requests.get("https://jsonplaceholder.typicode.com/users")

dados = resposta.json()

for dado in dados:
    print(dado["name"])