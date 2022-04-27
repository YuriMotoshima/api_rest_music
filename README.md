# api_rest_music

Api que busca as 10 musicas mais tocadas de um artista.

## Collection Externas

```py
async-timeout==4.0.2
certifi==2021.10.8
charset-normalizer==2.0.12
click==8.1.2
colorama==0.4.4
Deprecated==1.2.13
Flask==2.1.1
idna==3.3
importlib-metadata==4.11.3
itsdangerous==2.1.2
Jinja2==3.1.1
MarkupSafe==2.1.1
packaging==21.3
pyparsing==3.0.8
python-dotenv==0.20.0
redis==4.2.2
requests==2.27.1
urllib3==1.26.9
uuid==1.30
Werkzeug==2.1.1
wrapt==1.14.0
zipp==3.8.0
```

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