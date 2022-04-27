
# -*- coding: utf-8 -*-
import os
import re
import json

import urllib3
import requests

import redis
import uuid
from dotenv import load_dotenv

from libs.log import log
from libs.excepts import exceptions

urllib3.disable_warnings()


load_dotenv(dotenv_path=f"{os.getcwd()}\.env")
log().loginit()


_token = os.environ.get("TOKEN")
token = _token if 'Bearer' in _token else 'Bearer %s' % _token
headers = {'Content-Type': 'application/json', 'Authorization': _token}

def api_get_list_songs(artist:str) -> dict:
    """
    ### Função que consome a API songs do Genius.
    """
    headers = {'Content-Type': 'application/json', 'Authorization': token}
    endpoint = f'https://api.genius.com/search?q={artist}'
    session_request = requests.Session()
    try:
        response = session_request.get(endpoint, headers=headers)
        return response
    except Exception as e:
        raise exceptions(e)
    
def get_redis(redis_con:object, artist:str) -> str:
    """
    ### Função que consome REDIS e verifica se já existe uma consulta salva.
    """
    try:
        songs = redis_con.get(f"artista:{artist}")
        return songs
    except Exception as e:
        raise exceptions(e)

def put_redis(redis_con:object, artist:str, response:str, cache:bool = True) -> None:
    """
    ### Função que guarda no REDIS os dados da api.
    """
    try:
        if cache:
            key_id = f"artista:{artist}"
            redis_con.set(key_id, json.dumps(response), ex=604800)
    except Exception as e:
        raise exceptions(e)

def create_new_response(artist:str, response_api:dict) -> dict:
    """
    ### Função que trata o retorno da chamada personaliza uma responta
    """
    try:
        myuuid = uuid.uuid4()
        json_response = json.loads(response_api.content)
        if json_response['meta']['status'] == 200:
            list_song = [ r['result']['title'] for r in json_response['response']['hits'] ]
            response = {"status_code":json_response['meta']['status'], "artista":artist, "lista_musicas":list_song[0:10], "uuid":str(myuuid)}
        else:
            response = {"status_code":400, "message":"Bad Request"}
    except Exception as e:
        raise exceptions(e)
    
    return response


def run(artist:str, cache_res:bool = True) -> dict:
    """
    ### Função orquestradora.
    """
    try:
        red = redis.Redis(host=os.environ.get("HOST_REDIS"), port=os.environ.get("PORT_REDIS"), password=os.environ.get("PASS_REDIS"))
        get_songs_redis = get_redis(redis_con=red, artist=artist)
        if get_songs_redis:
            response = json.loads(get_songs_redis)
            return response
        else:
            response_api = api_get_list_songs(artist=artist)
            response = create_new_response(artist=artist, response_api=response_api)
            put_redis(redis_con=red, artist=artist, response=response, cache=cache_res)
            return response
    except Exception as e:
        raise exceptions(e)