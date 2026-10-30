import requests

dados = {
    "title":"Melhor texto",
    "body":"Amo ler livros",
    "userId":67
}

url = "https://jsonplaceholder.typicode.com/posts"
resposta = requests.post(url, json=dados)

print(resposta.status_code)
print(resposta.json())