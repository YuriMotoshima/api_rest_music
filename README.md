# api_rest_music

Api que busca as 10 musicas mais tocadas de um artista.


## Instalação

```
git clone https://github.com/YuriMotoshima/api_rest_music.git
```

## .env

```py
TOKEN= seu_token
HOST_REDIS= seu_host_redis
PORT_REDIS= porta_host_redis
PASS_REDIS= sua_senha_redis

LOGENV = DEV or PROD [ PROD remove urlib3 logs ]
LOGNAME = nome_arquivo_logs
DISABLELOG = True or False [False disabilita a criação de pasta e arquivo de logs, temos essa opção para utlização em plataformas como Google Cloud Platform, neste caso o logging apenas imprime da tela, sem salvar o log.]
```
## Endpoint

http://localhost/artist
## Exemplo de Valores de Entrada

```py
{
    "artista":"Kendrick Lamar",
    "cache":true
}

```
## Exemplo de Retorno - Sucesso

```py
{
    "artista": "Kendrick Lamar",
    "lista_musicas": [
        "HUMBLE.",
        "​m.A.A.d city",
        "Swimming Pools (Drank)",
        "DNA.",
        "Money Trees",
        "XXX.",
        "Bitch, Don’t Kill My Vibe",
        "King Kunta",
        "Poetic Justice",
        "LOVE."
    ],
    "status_code": 200,
    "uuid": "890adc6b-f572-45ff-9ae1-24aabb9e7856"
}

```
## Exemplo de Retorno - Erro

```py
{
    "message": "Bad Request",
    "status_code": 400
}

```