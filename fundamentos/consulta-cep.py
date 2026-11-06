import requests

cep = input("Digite um CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    print(resposta.status_code)
    print(resposta.json())

except requests.exceptions.RequestException:
    print("Erro na requisição!")