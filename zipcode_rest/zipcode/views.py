from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import EnderecoSerializer
from .models import Endereco
from .utils import busca_endereco


class Zipcode(ViewSet):

    def list(self, request):
        queryset = Endereco.objects.all()
        serializer = EnderecoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        cep = request.data['zip_code']
        endereco_completo = busca_endereco(cep)
        endereco = {
            'logradouro': endereco_completo.get('logradouro'),
            'bairro': endereco_completo.get('bairro'),
            'cidade': endereco_completo.get('cidade'),
            'uf': endereco_completo.get('estado'),
            'cep': endereco_completo.get('cep'),
        }
        serializer = EnderecoSerializer(data=endereco)
        if serializer.is_valid():
            endereco_novo = serializer.save()
            serializer_novo_endereco = EnderecoSerializer(endereco_novo)
            data = serializer_novo_endereco.data
            status = 201
        else:
            data = {'errors': serializer.errors}
            status = 400
        return Response(data=data, status=status)

    def retrieve(self, request, pk):
        queryset = Endereco.objects.all()
        endereco = get_object_or_404(queryset, pk=pk)
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)

    def destroy(self, request, pk):
        queryset = Endereco.objects.all()
        endereco = get_object_or_404(queryset, pk=pk)
        endereco.delete()
        return Response(data={'detail': 'sucess'}, status=200)
