# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CadastroFieis'
        db.create_table(u'cadastro_fieis_cadastrofieis', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('endereco', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('bairro', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('uf', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('cep', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('estadoCivil', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100)),
            ('dataNascimento', self.gf('django.db.models.fields.DateField')(max_length=10)),
            ('naturalDe', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cpf', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11)),
            ('tituloEleitor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('dataCasamento', self.gf('django.db.models.fields.DateField')(max_length=10)),
            ('conjuge', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('crente', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('dataConversaoDE', self.gf('django.db.models.fields.DateField')(max_length=10)),
            ('igrejaDE', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('orgpertenceDE', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('congregacaoDE', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dataBatismoDE', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('igrejaDBatismoDE', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('classeEBDDE', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cargosefuncoesDE', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recebidoCartaDataDE', self.gf('django.db.models.fields.DateField')(max_length=10)),
            ('igrejaOrigemDE', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('dataSaida', self.gf('django.db.models.fields.DateField')(max_length=10)),
            ('nomePai', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('nomeMae', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('area1PTS', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('funcao1PTS', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area2PTS', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('funcao2PTS', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area3PTS', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('funcao3PTS', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area4PTS', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('funcao4PTS', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'cadastro_fieis', ['CadastroFieis'])


    def backwards(self, orm):
        # Deleting model 'CadastroFieis'
        db.delete_table(u'cadastro_fieis_cadastrofieis')


    models = {
        u'cadastro_fieis.cadastrofieis': {
            'Meta': {'object_name': 'CadastroFieis'},
            'area1PTS': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'area2PTS': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'area3PTS': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'area4PTS': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cargosefuncoesDE': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'classeEBDDE': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'congregacaoDE': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'conjuge': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'crente': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dataBatismoDE': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'dataCasamento': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'dataConversaoDE': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'dataNascimento': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'dataSaida': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estadoCivil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'funcao1PTS': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'funcao2PTS': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'funcao3PTS': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'funcao4PTS': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igrejaDBatismoDE': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'igrejaDE': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'igrejaOrigemDE': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'naturalDe': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nomeMae': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nomePai': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'orgpertenceDE': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recebidoCartaDataDE': ('django.db.models.fields.DateField', [], {'max_length': '10'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tituloEleitor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['cadastro_fieis']