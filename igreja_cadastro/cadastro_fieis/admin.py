# coding: utf-8

from django.contrib import admin
from django.contrib.sites.models import Site
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _
from igreja_cadastro.cadastro_fieis.models import CadastroFieis

class CadastroFieisAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'criado_em', 'cadastrado_hoje')
    date_hierarchy = 'criado_em'
    search_fields = ('nome', 'email', 'cpf', 'criado_em')
    list_filter = ['criado_em']
    readonly_fields = ('image_tag',)

    def cadastrado_hoje(self, obj):
        return obj.criado_em.date() == datetime.today().date()

    cadastrado_hoje.short_description = _(u'Cadastrado Hoje?')
    cadastrado_hoje.boolean = True

admin.site.register(CadastroFieis, CadastroFieisAdmin)
admin.site.unregister(Site)