from collections import OrderedDict
from urllib.parse import urlunparse, urlencode

import requests

from .models import BuyerUserProfile, BuyerUser


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(
                              fields=','.join(('phone', 'email')),
                              access_token=response['access_token'],
                              v='5.199')),
                          None
                          ))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    if 'phone' in data and data['phone']:
        user.buyerprofile.phone_number = data['phone']
    if 'email' in data and data['email']:
        user.buyerprofile.email = data['email']
    user.save()
