from rest_framework import serializers
from .models import ZipCode


class ZipCodeSerializer(serializers.ModelSerializer):
    """Classe serialização dos dados recebidos na aplicação web
    para objetos compatíveis com o model "ZipCode" e vice versa.
    """
    class Meta:
        model = ZipCode
        fields = ('zip_code', 'address', 'neighborhood', 'city', 'state')
