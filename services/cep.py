import requests

# Função para validar o CEP
def verifica_cep(cep):
    print(cep)
    if '-' in cep:
        cep = cep.split('-')
        cep = f"{cep[0]}{cep[1]}"

    request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return request