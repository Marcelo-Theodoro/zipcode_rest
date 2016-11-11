import json
import requests


def busca_endereco(cep):
    URL = 'http://api.postmon.com.br/v1/cep/{}'.format(cep)
    r = requests.get(URL)
    d = json.loads(r.text)
    return d

if __name__ == '__main__':
    print(busca_endereco("14020260"))
