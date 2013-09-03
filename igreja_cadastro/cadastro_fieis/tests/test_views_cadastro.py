# coding: utf-8

"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from django.test import TestCase
from igreja_cadastro.cadastro_fieis.forms import CadastroForm


class CadastroTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastro/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'cadastro_fieis/cadastro_form.html')

    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 42)
        self.assertContains(self.resp, 'type="text"', 34)
        self.assertContains(self.resp, 'type="submit')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, CadastroForm)


class CadastroPostTest(TestCase):
    def setUp(self):
        data = dict(
            nome = 'Gilmar Soares'
            , sexo = 'Masculino'
            , endereco = 'Rua Luiz Gonzaga da Gama Filho'
            , numero = 149
            , bairro = 'Parque Peruche'
            , cidade = 'São Paulo'
            , uf = 'SP'
            , cep = '02539040'
            , estadoCivil = 'Solteiro'
            , telefone = '39514340'
            , celular = '980915395'
            , email = 'linux.soares@gmail.com'
            , dataNascimento = '1981-07-01'
            , naturalDe = 'São Paulo'
            , rg = '304447776'
            , cpf = '12345678901'
            , tituloEleitor = '98988989'
            , dataCasamento = '1990-04-04'
            , conjuge = 'Luciana A Costa'
            , crente = ''
            , dataConversaoDE = '1990-04-04'
            , igrejaDE = ''
            , orgpertenceDE = ''
            , congregacaoDE = ''
            , dataBatismoDE = '1990-04-04'
            , igrejaDBatismoDE = ''
            ,classeEBDDE = ''
            , cargosefuncoesDE = ''
            , recebidoCartaDataDE = '1990-04-04'
            , igrejaOrigemDE = ''
            , dataSaida = '1990-04-04'
            , nomePai = ''
            , nomeMae = ''
            , area1PTS = ''
            , funcao1PTS = ''
            , area2PTS = ''
            , funcao2PTS = ''
            , area3PTS = ''
            , funcao3PTS = ''
            , area4PTS = ''
            , funcao4PTS = ''
        )
        self.resp = self.client.post('/cadastro/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)