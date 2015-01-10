# -*- coding: utf-8 -*-
from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'data de criação')
    modified = models.DateTimeField(auto_now_add=True, auto_now=True, verbose_name=u'data de modificação')

    class Meta:
        abstract = True


class Servidor(TimeStampedModel):
    name = models.CharField(max_length=25, verbose_name='hostname')
    aplicacoes = models.ManyToManyField('Aplicacao')

    def __unicode__(self):
        return self.name


class Aplicacao(TimeStampedModel):
    name = models.CharField(max_length=25)
    # status

    def __unicode__(self):
        return self.name