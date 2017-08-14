import requests

TOKEN = 'fa02f64eebc06c838b50fca1a2b400e09c92fabac26627836be5283a8f16bd2f42146c3e5f986fa231464'
VERSION = '5.67'

params = {
    'access_token': TOKEN,
    'v': VERSION
}

def my_friends_id(params):
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()['response']['items']

print(my_friends_id(params))