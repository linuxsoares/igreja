# coding: utf-8

from django.test import TestCase
from igreja_cadastro.cadastro_fieis.forms import CadastroForm

class CadastroFormTest(TestCase):
    def test_has_fields(self):
        form = CadastroForm()
        self.assertItemsEqual(['nome', 'endereco', 'sexo', 'numero', 'bairro', 'cidade', 'uf', 'cep',
                               'estadoCivil', 'telefone', 'celular', 'email', 'dataNascimento', 'naturalDe',
                               'rg', 'cpf', 'tituloEleitor', 'dataCasamento', 'conjuge', 'crente', 'dataConversaoDE',
                               'igrejaDE', 'orgpertenceDE', 'congregacaoDE', 'dataBatismoDE', 'igrejaDBatismoDE',
                               'classeEBDDE', 'cargosefuncoesDE', 'recebidoCartaDataDE', 'igrejaOrigemDE', 'dataSaida',
                               'nomePai', 'nomeMae', 'area1PTS' , 'funcao1PTS', 'area2PTS' , 'funcao2PTS',
                               'area3PTS', 'funcao3PTS', 'area4PTS' , 'funcao4PTS'], form.fields)