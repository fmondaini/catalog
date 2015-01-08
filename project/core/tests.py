# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from tastypie.test import ResourceTestCase


class ResourcesTest(ResourceTestCase):
    def setUp(self):
        super(ResourcesTest, self).setUp()

        self.username = 'filipe'
        self.password = '123'
        self.user = User.objects.create_user(
            self.username,
            'filipe@mondaini.me',
            self.password)

    def get_credentials(self):
        return self.create_basic(username=self.username, password=self.password)

    def test_get_list_unauthorzied(self):
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/servidor/', format='json'))

    def test_get_list_servidor(self):
        resp = self.api_client.get('/api/v1/servidor/', format='json', authentication=self.get_credentials())
        self.assertValidJSONResponse(resp)

        # Conta quantos servidores estao cadastrados
        self.assertEqual(len(self.deserialize(resp)['objects']), 0)

    # TODO: 
    # cadastrar 1 servidor
    # cadastrar varios ao mesmo tempo
    # cadastrar 1 app
    # cadastrar varios apps ao mesmo tempo

    # validar update realizado em servidor/app

    # deletar 1 app
    # deletar varios apps
    # deletar 1 servidor
    # deletar varios servidores

    # validar schema aplicacao
    # validar schema servidor