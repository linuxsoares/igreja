# coding: utf-8

from django import forms
from django.utils.translation import ugettext as _

SEXO_CHOICES = (
    (0, 'Masculino'),(1, 'Feminino')
)

ESTADO_CIVIL = (
    (0, 'Solteiro(a)'),(1, 'Casado(a)')
)

class CadastroForm(forms.Form):
    nome = forms.CharField(label=_('Nome'))
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, label=_('Sexo'))
    endereco = forms.CharField(label=_('Endereco'))
    numero = forms.CharField(label=_('Numero'))
    bairro = forms.CharField(label=_('Bairro'))
    cidade = forms.CharField(label=_('Cidade'))
    uf = forms.CharField(label=_('UF'))
    cep = forms.CharField(label=_('CEP'))
    estadoCivil = forms.ChoiceField(choices=ESTADO_CIVIL, label=_('Estado Civil'))
    telefone = forms.CharField(label=_('Telefone'))
    celular = forms.CharField(label=_('Celular'))
    email = forms.CharField(label=_('E-mail'))
    dataNascimento = forms.CharField(label=_('Data de Nascimento'))
    naturalDe = forms.CharField(label=_('Natural De?'))
    rg = forms.CharField(label=_('RG'))
    cpf = forms.CharField(label=_('CPF'))
    tituloEleitor = forms.CharField(label=_('Titulo de Eleitor'))