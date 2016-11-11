from rest_framework import serializers
from .models import Endereco


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'logradouro', 'bairro', 'cidade', 'uf', 'cep')
