import json
import requests


def busca_endereco(cep):
    URL = 'http://api.postmon.com.br/v1/cep/{}'.format(cep)
    r = requests.get(URL)
    if r.status_code != 200:
        return False
    d = json.loads(r.text)
    return d


def valida_sintaxe_cep(cep):
    cep = str(cep).replace('-', '')
    return True if cep.isdigit() and len(cep) == 8 else False


if __name__ == '__main__':
    print(busca_endereco("14020260"))
