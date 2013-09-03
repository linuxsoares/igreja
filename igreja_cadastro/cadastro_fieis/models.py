# coding: utf-8

from django.db import models
from django.utils.translation import ugettext as _

class CadastroFieis(models.Model):

    SEXO = (
        (u'1', u'Masculino'),
        (u'2', u'Feminino'),
    )

    ESTADO_CIVIL = (
        (u'1', u'Solteiro(a)'),
        (u'2', u'Casado(a)'),
    )

    nome = models.CharField(_('nome'), max_length=100)
    sexo = models.CharField(choices=SEXO, max_length=20)
    endereco = models.CharField(_('endereco'), max_length=255)
    numero = models.CharField(_('numero'), max_length=10)
    bairro = models.CharField(_('bairro'), max_length=100)
    cidade = models.CharField(_('cidade'), max_length=150)
    uf = models.CharField(_('UF'), max_length=2)
    cep = models.CharField(_('CEP'), max_length=10)
    estadoCivil = models.CharField(choices=ESTADO_CIVIL, max_length=20)
    telefone = models.CharField(_('telefone'), max_length=10)
    celular = models.CharField(_('celular'), max_length=12)
    email = models.EmailField(_('e-mail'), max_length=100, unique=True)
    dataNascimento = models.DateField(_('data de nascimento'), max_length=12)
    naturalDe = models.CharField(_('natural de?'), max_length=150)
    rg = models.CharField(_('RG'), max_length=20, blank=True)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    tituloEleitor = models.CharField(_('titulo de eleitor'), max_length=20)
    dataCasamento = models.DateField(_('data de casamento'), max_length=10, blank=True)
    conjuge = models.CharField(_('conjuge'), max_length=200, blank=True)
    crente = models.CharField(_('crente'), max_length=3)
    dataConversaoDE = models.DateField(_('data conversao'), max_length=10, blank=True)
    igrejaDE = models.CharField(_('igreja'), max_length=100, blank=True)
    orgpertenceDE = models.CharField(_('org a que pertence'), max_length=200, blank=True)
    congregacaoDE = models.CharField(_('congregacao'), max_length=200, blank=True)
    dataBatismoDE = models.DateField(_('data de batismo'), max_length=10, blank=True)
    igrejaDBatismoDE = models.CharField(_('igreja'), max_length=150, blank=True)
    classeEBDDE = models.CharField(_('classe da ebd'), max_length=255, blank=True)
    cargosefuncoesDE = models.CharField(_('cargos/funcoes'), max_length=255, blank=True)
    recebidoCartaDataDE = models.DateField(_('recebido com carta? data:'), max_length=10, blank=True)
    igrejaOrigemDE = models.CharField(_('igreja de origem'), max_length=255, blank=True)
    dataSaida = models.DateField(_('data de saida:'), max_length=10, blank=True)
    nomePai = models.CharField(_('nome do pai:'), max_length=100, blank=True)
    nomeMae = models.CharField(_('nome da mae:'), max_length=100, blank=True)
    area1PTS = models.CharField(_('area'), max_length=200, blank=True)
    funcao1PTS = models.CharField(_('funcao'), max_length=200, blank=True)
    area2PTS = models.CharField(_('area'), max_length=200, blank=True)
    funcao2PTS = models.CharField(_('funcao'), max_length=200, blank=True)
    area3PTS = models.CharField(_('area'), max_length=200, blank=True)
    funcao3PTS = models.CharField(_('funcao'), max_length=200, blank=True)
    area4PTS = models.CharField(_('area'), max_length=200, blank=True)
    funcao4PTS = models.CharField(_('funcao'), max_length=200, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['criado_em']

    def __unicode__(self):
        return self.nome

