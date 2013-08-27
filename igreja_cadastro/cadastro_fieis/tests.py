"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from igreja_cadastro.cadastro_fieis.forms import CadastroForm


class CadastroTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastro/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'cadastro_fieis/cadastro_form.html')

    def test_html(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, 'type="submit')

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, CadastroForm)

    def test_form_has_fields(self):
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'endereco', 'sexo', 'numero', 'bairro', 'cidade'], form.fields)


