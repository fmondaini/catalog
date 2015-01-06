# Catalogo de servidores


Para fazer consultas nesta API, se faz necessário informar o `Content-Type` como `application/json` no Header


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
Serão criados automaticamente os atributos: `id`, `created` e `modified`

## Updates - Utilizando o verbo PUT
`PUT /api/v1/servidor/1/`