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

    def test_get_list_servidor(self):
        resp_admin = self.api_client.get('/api/v1/servidor/', format='json', authentication=self.get_credentials(username=self.admin))
        resp_user = self.api_client.get('/api/v1/servidor/', format='json', authentication=self.get_credentials(username=self.user))
        resp_unauthorized = self.api_client.get('/api/v1/servidor/', format='json')
        self.assertValidJSONResponse(resp_admin)
        self.assertValidJSONResponse(resp_user)
        self.assertHttpUnauthorized(resp_unauthorized)

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

    def test_get_list_aplicacao(self):
        resp_admin = self.api_client.get('/api/v1/aplicacao/', format='json', authentication=self.get_credentials(username=self.admin))
        resp_user = self.api_client.get('/api/v1/aplicacao/', format='json', authentication=self.get_credentials(username=self.user))
        resp_unauthorized = self.api_client.get('/api/v1/aplicacao/', format='json')

        self.assertValidJSONResponse(resp_admin)
        self.assertValidJSONResponse(resp_user)
        self.assertHttpUnauthorized(resp_unauthorized)

    def test_cadastrar_uma_aplicacao(self):
        post_data = {"name": "testapp"}

        resp_created = self.api_client.post(
            '/api/v1/aplicacao/',
            format='json',
            data=post_data,
            authentication=self.get_credentials(username=self.admin))
        resp_unauthorized = self.api_client.post(
            '/api/v1/aplicacao/',
            format='json',
            data=post_data,
            authentication=self.get_credentials(username=self.user))

        self.assertHttpCreated(resp_created)
        self.assertHttpUnauthorized(resp_unauthorized)

    def test_cadastrar_varias_aplicacoes(self): 
        post_data = {}
        for i in range(1,5):
            post_data["name"] = "app%d" % i

        resp_created = self.api_client.post(
            '/api/v1/aplicacao/',
            format='json',
            data=post_data,
            authentication=self.get_credentials(username=self.admin))
        resp_unauthorized = self.api_client.post(
            '/api/v1/aplicacao/',
            format='json',
            data=post_data,
            authentication=self.get_credentials(username=self.user))

        self.assertHttpCreated(resp_created)
        self.assertHttpUnauthorized(resp_unauthorized)

    def test_atualizar_servidor(self):
        post_data = {
            "aplicacoes": ["/api/v1/aplicacao/1/"]
        }
        resp_accepted = self.api_client.patch('/api/v1/servidor/1/', format='json', data=post_data, authentication=self.get_credentials(self.admin))
        resp_unauthorized = self.api_client.patch('/api/v1/servidor/1/', format='json', data=post_data, authentication=self.get_credentials(self.user))

        self.assertHttpAccepted(resp_accepted)
        self.assertHttpUnauthorized(resp_unauthorized)