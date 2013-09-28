#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        'Form must have 4 fields.'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'CPF must only accept digits.'
        form = self.make_validated_form(cpf='ABDC5678901')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF must have 11 digits.'
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_optional(self):
        'Email is optional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        'Email and Phone are optional, but one must be informed.'
        form = self.make_validated_form(email='', phone='')
        self.assertItemsEqual(['__all__'], form.errors)

    def test_name_must_be_capitalized(self):
        'Name must be capitalized.'
        form = self.make_validated_form(name='HENRIQUE bastos')
        self.assertEqual('Henrique Bastos', form.cleaned_data['name'])

    def test_name_with_connector_must_be_capitalized(self):
        'Name with connector must be capitalized correctly.'
        form = self.make_validated_form(name='jOHN DOS passos')
        self.assertEqual('John dos Passos', form.cleaned_data['name'])

    def make_validated_form(self, **kwargs):
        data = dict(name='Henrique Bastos', email='henrique@bastos.net',
                    cpf='12345678901', phone='21-96186180')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
