import requests

# Desafio 5 — Mini análise
# Mais difícil

# Busque os posts e descubra:
# - Quantos posts existem?
# - Quantos pertencem ao usuário 1?
# - Quantos pertencem ao usuário 2?
# - Qual usuário publicou mais?
# Treina: lógica, contadores e análise de dados.

url = "https://jsonplaceholder.typicode.com/posts"
resposta = requests.get(url)

dados = resposta.json()

contador = 0 # Posts
contador1 = 0 # userId 1
contador2 = 0 # userId 2

for dado in dados:
    contador += 1

    if dado["userId"] == 1:
        contador1 += 1

    if dado["userId"] == 2:
        contador2 += 1

print(f"O JSON tem {contador} posts.")
print(f"O user 1 tem {contador1} posts.")
print(f"O user 2 tem {contador2} posts.")

if contador1 > contador2:
    print("O usuário 1 publicou mais.")
elif contador2 > contador1:
    print("O usuário 2 publicou mais.")
else:
    print("Os dois usuários publicaram a mesma quantidade.")