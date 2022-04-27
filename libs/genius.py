
# -*- coding: utf-8 -*-
import os
import re
import json

import urllib3
import requests

from dotenv import load_dotenv

from libs.log import log
from libs.excepts import exceptions
urllib3.disable_warnings()

load_dotenv(dotenv_path=f"{os.getcwd()}\.env")
log().loginit()

_token = os.environ.get("TOKEN")
token = _token if 'Bearer' in _token else 'Bearer %s' % _token
headers = {'Content-Type': 'application/json', 'Authorization': _token}
endpoint = f'https://api.genius.com/songs/'


def request(query, headers={}, schema : str = "query"):
    _headers = headers
    _headers.update(headers)
    session_request = requests.Session()
    response = session_request.get(
        endpoint,
        headers=_headers, 
        verify=False
    )
    try:
        response = json.loads(response.text)
    except ValueError:
        raise exceptions(response.text)

    if response.get('error'):
        raise exceptions(response.get('error_description', response.get('error')))
    if response.get('errors'):
        for error in response.get('errors'):
            raise exceptions(error.get('message'))
    return response