#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
        else:
            return render(request,
                          'subscriptions/subscription_form.html',
                          {'form': form})
    else:
        return render(request,
                      'subscriptions/subscription_form.html',
                      {'form': SubscriptionForm()})
