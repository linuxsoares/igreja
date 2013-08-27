# coding: utf-8

from django import forms
from django.utils.translation import ugettext as _

SEXO_CHOICES = (
    (0, 'Masculino'),(1, 'Feminino')
)

class CadastroForm(forms.Form):
    name = forms.CharField(label=_('Nome'))
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, label=_('Sexo'))
    endereco = forms.CharField(label=_('Endereco'))
    numero = forms.CharField(label=_('Numero'))
    bairro = forms.CharField(label=_('Bairro'))
    cidade = forms.CharField(label=_('Cidade'))