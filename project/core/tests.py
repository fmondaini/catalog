# -*- coding: utf-8 -*-
from tastypie.test import ResourceTestCase


class ResourcesTest(ResourceTestCase):
    fixtures = ['data.json']

    def setUp(self):
        super(ResourcesTest, self).setUp()

        self.admin = 'filipe'
        self.user = 'beltrano'
        self.password = '123'

    def get_credentials(self, username):
        return self.create_basic(username=username, password=self.password)

    def test_get_list_unauthorzied(self):
        self.assertHttpUnauthorized(self.api_client.get('/api/v1/servidor/', format='json'))

    def test_get_list_servidor_ok(self):
        resp_admin = self.api_client.get('/api/v1/servidor/', format='json', authentication=self.get_credentials(username=self.admin))
        resp_user = self.api_client.get('/api/v1/servidor/', format='json', authentication=self.get_credentials(username=self.user))
        self.assertValidJSONResponse(resp_admin)
        self.assertValidJSONResponse(resp_user)

        # Conta quantos servidores estao cadastrados
        self.assertEqual(len(self.deserialize(resp_admin)['objects']), 5)
        self.assertEqual(len(self.deserialize(resp_user)['objects']), 5)

    def test_cadastrar_um_servidor(self): 
        post_data = {"name": "test"}

        resp_created = self.api_client.post(
            '/api/v1/servidor/',
            format='json',
            data=post_data,
            authentication=self.get_credentials(username=self.admin))
        resp_unauthorized = self.api_client.post(
            '/api/v1/servidor/',
            format='json',
            data=post_data,
            authentication=self.get_credentials(username=self.user))

        self.assertHttpCreated(resp_created)
        self.assertHttpUnauthorized(resp_unauthorized)

    def test_cadastrar_varios_servidores(self): 
        post_data = {}
        for i in range(1,5):
            post_data["name"] = "server%d" % i

        resp_created = self.api_client.post(
            '/api/v1/servidor/',
            format='json',
            data=post_data,
            authentication=self.get_credentials(username=self.admin))
        resp_unauthorized = self.api_client.post(
            '/api/v1/servidor/',
            format='json',
            data=post_data,
            authentication=self.get_credentials(username=self.user))

        self.assertHttpCreated(resp_created)
        self.assertHttpUnauthorized(resp_unauthorized)


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