# coding: utf-8
from xml.dom.minidom import Document

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from igreja_cadastro.cadastro_fieis.forms import CadastroForm
from igreja_cadastro.cadastro_fieis.models import CadastroFieis

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/cadastro/%d/' % obj.pk)
        else:
            return render(request, 'cadastro_fieis/cadastro_form.html', {'form': form})
    else:
        return render(request, 'cadastro_fieis/cadastro_form.html', {'form': CadastroForm()})

def detail(request, pk):
    cadastro_fiel = get_object_or_404(CadastroFieis, pk=pk)
    return render(request, 'cadastro_fieis/cadastro_detalhe.html', {'cadastro': cadastro_fiel})
