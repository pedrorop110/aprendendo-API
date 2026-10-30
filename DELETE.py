import requests

url = "https://jsonplaceholder.typicode.com/users/3" #/user/3

try:
    resposta = requests.delete(url)

    resposta.raise_for_status()

    print(f"Status: {resposta.status_code}")
    print(f"Respota: {resposta.json()}")

except requests.exceptions.RequestException:
    print("Deu erro.")