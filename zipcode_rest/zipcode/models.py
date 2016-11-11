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


class Endereco(models.Model):
    logradouro = models.CharField(max_length=120)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2, choices=UNIDADES_FEDERATIVAS)
    cep = models.CharField(max_length=8)

    def __str__(self):
        return self.cep
