# coding: utf-8
from Tkinter import Image

from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from igreja_cadastro.cadastro_fieis.models import CadastroFieis

def CPFValid(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF Deve conter apenas Números!'))

SEXO_CHOICES = (
    (0, 'Masculino'),(1, 'Feminino')
)

ESTADO_CIVIL = (
    (0, 'Solteiro(a)'),(1, 'Casado(a)')
)

class CadastroForm(forms.ModelForm):
    class Meta:
        model = CadastroFieis

    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].validators.append(CPFValid)
