#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind

    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs = qs.filter(kind=self.kind)
        return qs
