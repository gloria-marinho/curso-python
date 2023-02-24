import requests #Beautiful Soup 4 ou BS4 - permite destrinchar uma página web

texto = None

try:
    requisicao = requests.get("https://replit.com/") # o get pega as informações
    texto = requisicao.text  # o '.text' mostra o código-fonte da requisição
    print(texto)
except:
    print("Requisição deu erro")