import requests
from time import sleep

TOKEN = ''
VERSION = '5.67'

params = {
    'access_token': TOKEN,
    'v': VERSION
}

def my_friends_id(params):
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()['response']['items']

def mutual_friends():
    my_friends = my_friends_id(params)
    friends_id = set(my_friends_id(params))
    for my_friend_id in my_friends:
        params['user_id'] = my_friend_id
        friends_id = friends_id & set(requests.get('https://api.vk.com/method/friends.get', params))
        sleep(0.35)

mutual_friends()