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
            ('dataNascimento', self.gf('django.db.models.fields.DateField')(max_length=12)),
            ('naturalDe', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('rg', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('cpf', self.gf('django.db.models.fields.CharField')(unique=True, max_length=11)),
            ('tituloEleitor', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('dataCasamento', self.gf('django.db.models.fields.DateField')(max_length=10, blank=True)),
            ('conjuge', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('crente', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('dataConversaoDE', self.gf('django.db.models.fields.DateField')(max_length=10, blank=True)),
            ('igrejaDE', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('orgpertenceDE', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('congregacaoDE', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dataBatismoDE', self.gf('django.db.models.fields.DateField')(max_length=10, blank=True)),
            ('igrejaDBatismoDE', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('classeEBDDE', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cargosefuncoesDE', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('recebidoCartaDataDE', self.gf('django.db.models.fields.DateField')(max_length=10, blank=True)),
            ('igrejaOrigemDE', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dataSaida', self.gf('django.db.models.fields.DateField')(max_length=10, blank=True)),
            ('nomePai', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('nomeMae', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('area1PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('funcao1PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('area2PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('funcao2PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('area3PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('funcao3PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('area4PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('funcao4PTS', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('criado_em', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'cadastro_fieis', ['CadastroFieis'])


    def backwards(self, orm):
        # Deleting model 'CadastroFieis'
        db.delete_table(u'cadastro_fieis_cadastrofieis')


    models = {
        u'cadastro_fieis.cadastrofieis': {
            'Meta': {'ordering': "['criado_em']", 'object_name': 'CadastroFieis'},
            'area1PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'area2PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'area3PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'area4PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'bairro': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cargosefuncoesDE': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'cep': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'classeEBDDE': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'congregacaoDE': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'conjuge': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'crente': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'criado_em': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dataBatismoDE': ('django.db.models.fields.DateField', [], {'max_length': '10', 'blank': 'True'}),
            'dataCasamento': ('django.db.models.fields.DateField', [], {'max_length': '10', 'blank': 'True'}),
            'dataConversaoDE': ('django.db.models.fields.DateField', [], {'max_length': '10', 'blank': 'True'}),
            'dataNascimento': ('django.db.models.fields.DateField', [], {'max_length': '12'}),
            'dataSaida': ('django.db.models.fields.DateField', [], {'max_length': '10', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'endereco': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estadoCivil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'funcao1PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'funcao2PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'funcao3PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'funcao4PTS': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igrejaDBatismoDE': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'igrejaDE': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'igrejaOrigemDE': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'naturalDe': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nomeMae': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'nomePai': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'orgpertenceDE': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'recebidoCartaDataDE': ('django.db.models.fields.DateField', [], {'max_length': '10', 'blank': 'True'}),
            'rg': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tituloEleitor': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'uf': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['cadastro_fieis']