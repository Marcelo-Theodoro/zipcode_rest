# zipcode_rest



_____________

## Como instalar


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
