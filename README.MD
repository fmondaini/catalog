# Catalogo de servidores e aplicações

[![Build Status](https://travis-ci.org/fmondaini/catalog.svg?branch=master)](https://travis-ci.org/fmondaini/catalog)

## Instalação no ambiente local:
* Faça um clone do projeto
* Crie um novo virtualenv e ative-o.
* Instale com o pip as dependencias com o comando: `pip install -r requirements.txt`

* Banco de dados:
Na pasta `project` execute `python manage.py migrate`, a seguir execute `python manage.py loaddata core/fixtures/data.json`


## Execução: 
Para rodar o projeto execute `python manage.py runserver`


## Uso da API
Para fazer consultas nesta API, se faz necessário informar o `Content-Type` como `application/json` no Header. Também se faz necessário autenticar com um usuário/senha.


## Consultas - utilizando o verbo GET
`GET /api/v1/servidor/`
`GET /api/v1/servidor/1`

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