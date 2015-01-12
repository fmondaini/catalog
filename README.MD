# Catalogo de servidores e aplicações

[![Build Status](https://travis-ci.org/fmondaini/catalog.svg?branch=master)](https://travis-ci.org/fmondaini/catalog)

## Instalação no ambiente local:
* Faça um clone do projeto
* Crie um novo virtualenv e ative-o.
* Instale com o pip as dependencias com o comando: `pip install -r requirements.txt`

* Banco de dados:
Execute `python manage.py migrate`, a seguir execute `python manage.py loaddata core/fixtures/data.json`


## Execução: 
Para rodar o projeto execute `python manage.py runserver`


## Uso da API
Para fazer consultas nesta API, se faz necessário informar o `Content-Type` como `application/json` no Header. Também se faz necessário autenticar com um usuário/senha: [Basic Authentication](http://en.wikipedia.org/wiki/Basic_access_authentication)

## Listar endpoints:
`GET /api/v1/`

Resultado: 
```
{
    aplicacao: {
        list_endpoint: "/api/v1/aplicacao/",
        schema: "/api/v1/aplicacao/schema/"
},
    servidor: {
        list_endpoint: "/api/v1/servidor/",
        schema: "/api/v1/servidor/schema/"
    }
}
```

## Consultas - utilizando o verbo GET
### Exemplo 1 - Listando todos os servidores:
`GET /api/v1/servidor/`

Resultado:
```
{
    "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 4},
    "objects": [
    {
        "aplicacoes": [{
            "created": "2015-01-07T16:19:30.767991",
            "id": 1,
            "modified": "2015-01-07T16:19:30.768032",
            "name": "app1",
            "resource_uri": "/api/v1/aplicacao/1/"},
            {
            "created": "2015-01-07T18:34:03.601974",
            "id": 2,
            "modified": "2015-01-07T18:34:03.602015",
            "name": "g1",
            "resource_uri": "/api/v1/aplicacao/2/"}],
        "created": "2015-01-06T03:03:03",
        "id": 1,
        "modified": "2015-01-07T18:37:16.617600",
        "name": "test 2",
        "resource_uri": "/api/v1/servidor/1/"
    },
    {
        "aplicacoes": [ ],
        "created": "2015-01-06T19:45:42.142530",
        "id": 2,
        "modified": "2015-01-06T19:45:42.142567",
        "name": "qa01",
        "resource_uri": "/api/v1/servidor/2/"
    },
}

```

### Exemplo 2 - Consultando servidor pelo ID
`GET /api/v1/servidor/1`

Resultado:
```
{
    "aplicacoes": [{
        "created": "2015-01-07T16:19:30.767991",
        "id": 1,
        "modified": "2015-01-07T16:19:30.768032",
        "name": "app1",
        "resource_uri": "/api/v1/aplicacao/1/"
    },
    {
        "created": "2015-01-07T18:34:03.601974",
        "id": 2,
        "modified": "2015-01-07T18:34:03.602015",
        "name": "g1",
        "resource_uri": "/api/v1/aplicacao/2/"
    }],
    "created": "2015-01-06T03:03:03",
    "id": 1,
    "modified": "2015-01-07T18:37:16.617600",
    "name": "qa01",
    "resource_uri": "/api/v1/servidor/1/"
}
```

## Inclusões - Utilizando o verbo POST
`POST /api/v1/servidor/`

O json deve ser enviado no formato:
```
{
    "name": "hostname"
}
```
Serão criados automaticamente os atributos: `id`, `created`, `modified` e `aplicacoes`


## Updates - Utilizando o verbo PATCH
`PATCH /api/v1/servidor/1/`

Exemplo de JSON atualizando aplicações ao servidor:
```
{
    "aplicacoes": [
        "/api/v1/aplicacao/1",
        "/api/v1/aplicacao/3"
    ]
}
```

## Deletar - Utilizando o verbo DELETE
`DELETE /api/v1/servidor/1`
`DELETE /api/v1/aplicacao/1`