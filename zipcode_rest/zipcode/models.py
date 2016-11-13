from django.db import models


class ZipCode(models.Model):
    """Classe que representa a tabela ZipCode no banco de dados.

    O atributo "zip_code" é a chave primária(pk) da tabela.
    """
    zip_code = models.CharField(max_length=8, primary_key=True)
    # Existem CEPs gerais que não tem informações sobre
    # endereço e logradouro. Estes campos podem ser deixados
    # em branco.
    address = models.CharField(max_length=120, blank=True)
    neighborhood = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=2)

    def __str__(self):
        """Retorna uma string que representa o objeto"""
        return self.zip_code
