# -*- coding: utf-8 -*-
from tastypie.resources import ModelResource
from core.models import Servidor, Aplicacao


class ServidorResource(ModelResource):
    class Meta:
        queryset = Servidor.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']


class AplicacaoResource(ModelResource):
    class Meta:
        queryset = Aplicacao.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']