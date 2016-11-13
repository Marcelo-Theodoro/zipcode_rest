from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import ZipCodeSerializer
from .models import ZipCode
from .utils import busca_endereco
from .utils import valida_sintaxe_cep


class Zipcode(ViewSet):
    """Interface para adição, listagem e exclusão de
    zipcodes.
    """

    def list(self, request):
        """Lista os zipcodes cadastrados.
        Caso a requisição seja realizada contendo a
        query string "limit", o método vai retornar um máximo
        de itens setado em "limit". Caso "limit" seja False,
        ou None, retorna todos os itens salvos.
        Método HTTP aceito: GET
        """

        # Cria o objeto(lazy) query contendo os registros
        # de todos os zipcodes cadastrados no sistema.
        queryset = ZipCode.objects.all()
        # Verificamos se a querystring foi setada
        # na requisição.
        limit = request.GET.get('limit')
        if limit:
            try:
                # Verificamos se o valor de limit é válido.
                # O único tipo de valor válido nesse caso, é inteiro.
                limit = int(limit)
            except ValueError:
                # Caso alguma exceção seja capturada ao tentar
                # transformar o valor de limit para inteiro,
                # é retornado ao usuário uma mensagem de erro
                # e o status code 400 BAD REQUEST
                return Response(data={'errors': 'valor limit inválido'},
                                status=400)
            else:
                # Caso nenhuma exception seja capturada, o queryset
                # é limitado ao valor solicitado pelo usuário
                # através de slices.
                queryset = queryset[:limit]
        # O objeto queryset é serializado para ser retornado ao usuário.
        serializer = ZipCodeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Insere um novo registro no banco de dados.
        Método HTTP aceito: POST
        """

        cep = request.data['zip_code']
        # Verifica se a sintaxe do CEP está correta. Ou seja,
        # se ele é composto de 8 dígitos.
        if not valida_sintaxe_cep(cep):
            # Caso a sintaxe esteja errada, retorna um erro ao usuário.
            # Dessa forma não é necessário gastar recursos fazendo
            # uma requisição para o serviço externo.
            return Response(data={'errors': 'CEP inválido'}, status=400)
        # Busca informações do CEP.
        endereco_completo = busca_endereco(cep)
        # Verifica se as informações foram retornadas com sucesso.
        if not endereco_completo:
            return Response(data={'errors': 'CEP não encontrado'}, status=400)
        # Separa as informações relevantes no nosso caso, e cria
        # um dicionário com as chaves compatíveis com os models, e
        # pronto para ser validado.
        endereco = {
            'address': endereco_completo.get('logradouro', ''),
            'neighborhood': endereco_completo.get('bairro', ''),
            'city': endereco_completo.get('cidade'),
            'state': endereco_completo.get('estado'),
            'zip_code': endereco_completo.get('cep'),
        }
        # Executa a classe serializadora.
        serializer = ZipCodeSerializer(data=endereco)
        # Verifica se os dados são válidos de acordo
        # com as regras definidas nos models.
        if serializer.is_valid():
            # Salva as informações no banco de dados
            # e retorna o objeto recém criado para o usuário,
            # junto com o código 201 CREATED.
            endereco_novo = serializer.save()
            serializer_novo_endereco = ZipCodeSerializer(endereco_novo)
            data = serializer_novo_endereco.data
            status = 201
        else:
            # Retorna uma mensagem contendo os erros encontrados
            # junto com o código 400 BAD REQUEST
            data = {'errors': serializer.errors}
            status = 400
        return Response(data=data, status=status)

    def retrieve(self, request, pk):
        """Retorna detalhes de um objeto em específico.
        Método HTTP aceito: GET
        """

        queryset = ZipCode.objects.all()
        # Busca um objeto no queryset utilizando
        # a chave primária(pk) recebida.
        # Caso não encontre, retorna 404 NOT FOUND.
        endereco = get_object_or_404(queryset, pk=pk)
        # Serializa o registro encontrado e retorna.
        serializer = ZipCodeSerializer(endereco)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Exclui da base de dados um zipcode em específico.
        Método HTTP aceito: DELETE
        """

        queryset = ZipCode.objects.all()
        # Busca um objeto no queryset utilizando
        # a chave primária(pk) recebida.
        # Caso não encontre, retorna 404 NOT FOUND.
        endereco = get_object_or_404(queryset, pk=pk)
        # Executa a exclusão.
        endereco.delete()
        # Retorna código de status 204 No Content para confirmar
        # a exclusão.
        return Response(data={}, status=204)
