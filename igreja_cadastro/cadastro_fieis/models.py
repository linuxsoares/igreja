# coding: utf-8

from django.db import models
from django.utils.translation import ugettext as _

class CadastroFieis(models.Model):

    SEXO = (
        (0, 'Masculino'),
        (1, 'Feminino'),
    )

    ESTADO_CIVIL = (
        (0, 'Solteiro(a)'),
        (1, 'Casado(a)'),
    )

    nome = models.CharField(_('nome'), max_length=100)
    sexo = models.CharField(choices=SEXO, max_length=20)
    endereco = models.CharField(_('endereco'), max_length=255)
    numero = models.CharField(_('numero'), max_length=10)
    bairro = models.CharField(_('bairro'), max_length=100)
    cidade = models.CharField(_('cidade'), max_length=150)
    uf = models.CharField(_('UF'), max_length=2)
    cep = models.CharField(_('CEP'), max_length=7)
    estadoCivil = models.CharField(choices=ESTADO_CIVIL, max_length=20)
    telefone = models.CharField(_('telefone'), max_length=10)
    celular = models.CharField(_('celular'), max_length=12)
    email = models.EmailField(_('e-mail'), max_length=100, unique=True)
    dataNascimento = models.DateField(_('data de nascimento'), max_length=10)
    naturalDe = models.CharField(_('natural de?'), max_length=150)
    rg = models.CharField(_('RG'), max_length=20)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    tituloEleitor = models.CharField(_('titulo de eleitor'), max_length=20)
    dataCasamento = models.DateField(_('data de casamento'), max_length=10)
    conjuge = models.CharField(_('conjuge'), max_length=200)
    crente = models.CharField(_('crente'), max_length=3)
    dataConversaoDE = models.DateField(_('data conversao'), max_length=10)
    igrejaDE = models.CharField(_('igreja'), max_length=100)
    orgpertenceDE = models.CharField(_('org a que pertence'), max_length=200)
    congregacaoDE = models.CharField(_('congregacao'), max_length=200)
    dataBatismoDE = models.CharField(_('data de batismo'), max_length=10)
    igrejaDBatismoDE = models.CharField(_('igreja'), max_length=150)
    classeEBDDE = models.CharField(_('classe da ebd'), max_length=255)
    cargosefuncoesDE = models.CharField(_('cargos/funcoes'), max_length=255)
    recebidoCartaDataDE = models.DateField(_('recebido com carta? data:'), max_length=10)
    igrejaOrigemDE = models.CharField(_('igreja de origem'), max_length=255)
    dataSaida = models.DateField(_('data de saida:'), max_length=10)
    nomePai = models.DateField(_('nome do pai:'), max_length=100)
    nomeMae = models.DateField(_('nome da mae:'), max_length=100)
    area1PTS = models.DateField(_('area'), max_length=200)
    funcao1PTS = models.DateField(_('funcao'), max_length=200)
    area2PTS = models.DateField(_('area'), max_length=200)
    funcao2PTS = models.DateField(_('funcao'), max_length=200)
    area3PTS = models.DateField(_('area'), max_length=200)
    funcao3PTS = models.DateField(_('funcao'), max_length=200)
    area4PTS = models.DateField(_('area'), max_length=200)
    funcao4PTS = models.DateField(_('funcao'), max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nome