# coding: utf-8

from django.test import TestCase
from datetime import datetime
from django.db import IntegrityError
from igreja_cadastro.cadastro_fieis.models import CadastroFieis

class CadastroFieisTest(TestCase):
    def setUp(self):
        self.obj = CadastroFieis(
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

    def test_create(self):
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        self.obj.save()
        self.assertIsInstance(self.obj.criado_em, datetime)