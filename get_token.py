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

TOKEN = '59e4d2be565e6c2922989930df74e6a6a4daf63475c31195f3d469d629c6c8baafd74c96141d7a5f679c6'
