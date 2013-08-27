# coding: utf-8

from django.shortcuts import render
from igreja_cadastro.cadastro_fieis.forms import CadastroForm

def cadastro(request):
    return render(request, 'cadastro_fieis/cadastro_form.html', {'form': CadastroForm()})
