# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CadastroFieis'
        db.delete_table(u'cadastro_fieis_cadastrofieis')


    def backwards(self, orm):
        # Adding model 'CadastroFieis'
        db.create_table(u'cadastro_fieis_cadastrofieis', (
            ('tituloEleitor', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('funcao3PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('area1PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dataBatismoDE', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('orgpertenceDE', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('nomeMae', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('igrejaDE', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('igrejaDBatismoDE', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('area4PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dataConversaoDE', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('funcao4PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dataCasamento', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('congregacaoDE', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('estadoCivil', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('recebidoCartaDataDE', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('classeEBDDE', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('conjuge', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area2PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dataSaida', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('naturalDe', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nomePai', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('dataNascimento', self.gf('django.db.models.fields.DateField')(max_length=12)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100, unique=True)),
            ('cargosefuncoesDE', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('funcao2PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('crente', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('igrejaOrigemDE', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('cpf', self.gf('django.db.models.fields.CharField')(max_length=11, unique=True)),
            ('funcao1PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('area3PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cadastro_fieis', ['CadastroFieis'])


    models = {
        
    }

    complete_apps = ['cadastro_fieis']