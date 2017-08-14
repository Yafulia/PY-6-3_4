from pprint import pprint
from urllib.parse import urlencode

import requests

AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
APP_ID = 6144178
VERSION = '5.67'

auth_data = {
    'client_id': APP_ID,
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'display': 'mobile',
    'scope': 'friends,status,video,wall',
    'response_type': 'token',
    'v': VERSION
}

#print('?'.join(
#    (AUTHORIZE_URL, urlencode(auth_data))
#))

TOKEN = ''
