# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.resources import ModelResource

from core.models import Servidor, Aplicacao


class ServidorResource(ModelResource):
    aplicacoes = fields.ToManyField('core.api.resources.AplicacaoResource', 'aplicacoes', full=True, null=True)

    class Meta:
        queryset = Servidor.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete', 'patch']


class AplicacaoResource(ModelResource):
    class Meta:
        queryset = Aplicacao.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
