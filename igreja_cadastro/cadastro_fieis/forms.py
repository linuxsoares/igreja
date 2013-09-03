# coding: utf-8

from django import forms
from django.utils.translation import ugettext as _
from igreja_cadastro.cadastro_fieis.models import CadastroFieis

SEXO_CHOICES = (
    (0, 'Masculino'),(1, 'Feminino')
)

ESTADO_CIVIL = (
    (0, 'Solteiro(a)'),(1, 'Casado(a)')
)

class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroFieis