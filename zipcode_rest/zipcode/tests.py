from time import sleep
from random import randint
from django.test import TestCase
from django.test import RequestFactory
from django.http import Http404
from .utils import valida_sintaxe_cep
from .utils import busca_endereco
from .models import ZipCode
from .views import Zipcode


# class UtilsTestCase(TestCase):
#
#     def test_valida_sintaxe_cep_correta(self):
#         sintaxes_corretas = [19914310, '19914310', '19914-310']
#         for s in sintaxes_corretas:
#             self.assertTrue(valida_sintaxe_cep(s))
#
#     def test_valida_sintaxe_cep_incorreta(self):
#         sintaxes_incorretas = [199143101, 1991431, '19914d310', '199143100',
#                                'teste']
#         for s in sintaxes_incorretas:
#             self.assertFalse(valida_sintaxe_cep(s))
#
#     def test_busca_endereco_cep_valido(self):
#         cep_validos = [19914310, '19914310', '19914-310']
#         for cep in cep_validos:
#             sleep(1)
#             self.assertEqual(busca_endereco(cep)['cep'], '19914310')
#
#     def test_busca_endereco_cep_invalido(self):
#         cep_invalidos = [199143101, 1991431, '19914d310', '199143100']
#         for cep in cep_invalidos:
#             sleep(1)
#             self.assertEqual(busca_endereco(cep), False)


class ViewsTestCase(TestCase):

    def setUp(self):
        self.CEPS = set()
        for i in range(100):
            self.CEPS.add(randint(11111111, 99999999))
        for cep in self.CEPS:
            d = {
                'zip_code': cep,
                'address': 'teste',
                'neighborhood': 'teste',
                'city': 'teste',
                'state': 'SP',
                }
            ZipCode.objects.create(**d)
        self.factory = RequestFactory()
        self.view = Zipcode()

    def test_buscar_todos_registros(self):
        request = self.factory.get('/zipcodes/')
        response = self.view.list(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), len(self.CEPS))

    def test_buscar_registros_com_limit_valido(self):
        LIMITE = 12
        request = self.factory.get('/zipcodes/?limit={}'.format(LIMITE))
        response = self.view.list(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), LIMITE)

    def test_buscar_registros_com_limit_invalido(self):
        LIMITE = 'teste'
        request = self.factory.get('/zipcodes/?limit={}'.format(LIMITE))
        response = self.view.list(request)
        self.assertEqual(response.status_code, 400)

    def test_buscar_registro_especifico_existente(self):
        registro = ZipCode.objects.all().first().pk
        request = self.factory.get('/zipcodes/{}/'.format(registro))
        response = self.view.retrieve(request, registro)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['zip_code'], registro)

    def test_buscar_registro_especifico_inexistente(self):
        registro = 1111110
        request = self.factory.get('/zipcodes/{}/'.format(registro))
        with self.assertRaises(Http404):
            self.view.retrieve(request, registro)

    def test_deletar_registro(self):
        registro = ZipCode.objects.all().first().pk
        request = self.factory.delete('/zipcodes/{}/'.format(registro))
        response = self.view.destroy(request, registro)
        self.assertEqual(ZipCode.objects.filter(pk=registro).exists(), False)
        self.assertEqual(response.status_code, 204)

    def test_criar_registro_valido(self):
        CEP = '19914-310'
        request = self.factory.post('/zipcodes/')
        # O atributo .data é utilizado pelo DRF(Django Rest Framework)
        # para disponibilizar informações do request.post
        # já parseadas e pronto para o uso.
        # Como o DRF utiliza a classe Request ao invés da
        # HttpRequest que está sendo utilizada nessas simulações,
        # é necessário criar o atributo .data manualmente.
        # Ref: http://www.django-rest-framework.org/api-guide/requests/
        request.data = {'zip_code': CEP}
        response = self.view.create(request)
        zip_code_criado = response.data['zip_code']
        self.assertEqual(zip_code_criado, CEP.replace('-', ''))
        self.assertEqual(ZipCode.objects.filter(pk=zip_code_criado).exists(),
                         True)
        self.assertEqual(response.status_code, 201)

    def test_criar_registro_cep_invalido(self):
        CEP = '1402-260'
        request = self.factory.post('/zipcodes/')
        request.data = {'zip_code': CEP}
        response = self.view.create(request)
        self.assertEqual(response.status_code, 400)
#

    def test_criar_registro_cep_geral(self):
        CEP = '86455000'
        request = self.factory.post('/zipcodes/')
        request.data = {'zip_code': CEP}
        response = self.view.create(request)
        self.assertEqual(response.status_code, 201)

    def test_criar_registro_cep_inexistente(self):
        CEP = '11111111'
        request = self.factory.post('/zipcodes/')
        request.data = {'zip_code': CEP}
        response = self.view.create(request)
        self.assertEqual(response.status_code, 400)

    def test_criar_registro_cep_ja_cadastrado(self):
        CEP = '19914-310'
        request = self.factory.post('/zipcodes/')
        request.data = {'zip_code': CEP}
        response = self.view.create(request)
        response = self.view.create(request)
        self.assertEqual(response.status_code, 400)


class ModelsTestCase(TestCase):

    def test_representacao_model(self):
        d = {
            'zip_code': '19914320',
            'address': 'teste',
            'neighborhood': 'teste',
            'city': 'teste',
            'state': 'SP',
            }
        r = ZipCode.objects.create(**d)
        self.assertEqual(str(r), '19914320')
