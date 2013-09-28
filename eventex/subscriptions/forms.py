#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription


def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))
    if len(value) != 11:
        raise ValidationError(_(u'CPF deve ter 11 números'))


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].validators.append(CPFValidator)

    def clean_name(self):
        no_capitalize = ['da', 'de', 'do', 'das', 'dos']
        name = self.cleaned_data['name']
        words = name.split()
        for index, word in enumerate(words):
            if word.lower() in no_capitalize:
                words[index] = word.capitalize()
            else:
                words[index] = word.lower()
        capitalized_name = ' '.join(words)
        return capitalized_name
