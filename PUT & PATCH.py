import requests

# PUT = É um método HTTP usado para atualizar ou substituir completamente as informações de um recurso que já existe no servidor.
# PATCH = Altera parcialmente um recurso.

try:
    url = "https://jsonplaceholder.typicode.com/users/2"

    dados = {
        "name": "Pedro",
        "age":18,
        "city":"CDA"
    }

    resposta = requests.patch(url, json=dados) # Se eu tivesse usado o PUT os outros poderiam ter sido excluidos.

    print(resposta.status_code)
    print(resposta.json())

except requests.exceptions.RequestException:
    print("Houve um erro.")