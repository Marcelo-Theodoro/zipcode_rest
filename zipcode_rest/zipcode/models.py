from django.db import models


UNIDADES_FEDERATIVAS = (
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PR', 'PR'),
    ('PB', 'PB'),
    ('PA', 'PA'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SE', 'SE'),
    ('SP', 'SP'),
    ('TO', 'TO'),
    )


class ZipCode(models.Model):
    """Classe que representa a tabela ZipCode no banco de dados.

    O atributo "zip_code" é a chave primária(pk) da tabela.
    O atributo "state" aceita como entrada apenas os itens
    que estão na tupla "UNIDADES_FEDERATIVAS".
    """
    zip_code = models.CharField(max_length=8, primary_key=True)
    address = models.CharField(max_length=120)
    neighborhood = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2, choices=UNIDADES_FEDERATIVAS)

    def __str__(self):
        """Retorna uma string que representa o objeto"""
        return self.zip_code
