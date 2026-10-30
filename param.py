import requests

try:
    url = "https://jsonplaceholder.typicode.com/users"

    parametro = {
        "id": 2
}

    resposta = requests.get(url, params=parametro)

    status = resposta.status_code
    if status == 200:
        print("Status = Tudo Certo!")

    print(resposta.json())

except requests.exceptions.RequestException:
    print("Ta dando erro.")