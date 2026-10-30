import requests

try:
    url = "https://jsonplaceholder.typicode.com/users"

    dados = {
        "name": "Pedro Lucas",
        "age":18,
        "city":"CDA"
    }

    resposta = requests.post(url, json=dados)

    print(resposta.status_code)
    print(resposta.json())

except requests.exceptions.RequestException:
    print("Houve um erro.")