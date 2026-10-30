import requests

#DESAFIO FÁCIL = Desafio 2 — Contagem
# Usando a mesma API, conte quantos usuários possuem website cadastrado.
# Mostre o total no final.

url =  "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url)

dados = resposta.json()

contador = 0
for dado in dados:
    if dado["website"]:
        print(f"{dado['name']} tem o site -> {dado['website']}")
        contador += 1

print(f"\nExistem {contador} pessoas diferentes que possuem um site.\n")