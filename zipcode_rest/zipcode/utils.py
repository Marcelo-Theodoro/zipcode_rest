import json
import requests


def busca_endereco(cep):
    """Função que recebe uma string que representa um CEP
    e busca informações sobre esse CEP serviço externo.
    Caso a requisição não tenha sucesso ou o CEP seja inválido,
    retorna False.
    """
    URL = 'http://api.postmon.com.br/v1/cep/{}'.format(cep)
    r = requests.get(URL)
    if r.status_code != 200:
        return False
    d = json.loads(r.text)
    return d


def valida_sintaxe_cep(cep):
    """Função que verificar se a sintaxe de uma string recebida
    é compatível com a sintaxe de um CEP.
    Retorna True caso seja compatível, False caso contrario.
    """
    cep = str(cep).replace('-', '')
    return True if cep.isdigit() and len(cep) == 8 else False
