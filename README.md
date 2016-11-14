# zipcode_rest

REST app que permite a inserção, exclusão, listagem e detalhamento de CEPs.


Aplicação desenvolvida utilizando:

* [Python 3](https://www.python.org/)

* [Django](https://github.com/django/django)

* [Django Rest Framework](https://github.com/tomchristie/django-rest-framework)

* [PostmonAPI](https://github.com/PostmonAPI/postmon)

_____________

## Documentação dos recursos

| Descrição  | Recurso | Método | URL Param | Data Params | HTTP Response em caso de sucesso | Exemplo | 
| ------------- | ------------- |------------- |------------- |------------- |------------- |-------------|
| Listar registros | /zipcode/ | GET |  Optional: `limit=[numeric]` | None | 200 | `curl http://127.0.0.1:8000/zipcode/limit=2`
| Inserir registro | /zipcode/ | POST| None | `zip_code=[CEP]` | 201 | `curl --data "zip_code=14020260" http://localhost:8000/zipcode/`
| Exibir detalhes  | /zipcode/[CEP]/ | GET | None | None | 200 | `curl http://localhost:8000/zipcode/14020260/`
| Deletar registro  | /zipcode/[CEP]/ | DELETE | None | None | 204 | `curl -X DELETE http://localhost:8000/zipcode/14020260/`


_____________

## Cobertura dos testes

| Name | Stmts | Miss | Cover |
| ---- | ----- | ---- | ----- |
| zipcode/utils.py | 12 | 0 | 100% |
| zipcode/views.py | 46 | 0 | 100% |
| serializers.py | 6 | 0 | 100% |

_____________

## Instalação


Sistema operacional: Compatível com sistema de pacotes Debian, como Ubuntu, Mint. Em outros sistema operacionais é necessário a alteração dos comandos baseados em `apt-get` para seu equivalente na distribuição, como o `dnf` no caso do Fedora, por exemplo.

### Instalação dos pacotes necessários:

```bash
$ apt-get install python-pip git
```


### Instalação, criação e ativação de um virtual environment.

A utilização de um `virtualenv`, apesar de não obrigatória, é recomendada pela possibilidade de manter isolado o ambiente da aplicação, de outras aplicações existentes na máquina instalada.

Instalação do aplicativo `virtualenv` através do PyPI:

```bash
$ pip install virtualenv
```


Criação do virtualenv:

```bash
virtualenv -p python3 zipcode
```


Ativação do `virtualenv`:

```bash
$ source zipcode/bin/activate
```

### Download da aplicação

```bash
$ git clone https://github.com/Marcelo-Theodoro/zipcode_rest.git
```

### Instalação das dependências

```bash
$ cd zipcode_rest
$ pip install -r requirements.txt
```

### Criação do banco de dados

```bash
$ cd zipcode_rest
$ python manage.py makemigrations
$ python manage.py migrate
```


### Execução dos testes

```bash
$ python manage.py test
```

Os testes já estão integrados com a biblioteca [coverage](https://coverage.readthedocs.io/en/coverage-4.2/), e irão exibir a informação sobre a cobertura dos testes após a finalização destes.



### Inicialização do servidor de desenvolvimento e testes

```bash
python manage.py runserver
```


_____________

## LOGS

A aplicação está configurada armazenar logs de todas as ações no arquivo `zipcode.log` que se encontra na raiz da aplicação.

O modelo dos logs segue: datetime - Level - Action 

Exemplo:

| datetime | Level | Action 
| -------- | ----- | ---- |
1479034455.157838 | INFO | "POST /zipcode/ HTTP/1.1" 201 132 |
