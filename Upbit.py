import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

access_key = "HonSESgy9OMkRojjntP6AunVk1ZlA10i0J4tHuJN"
secret_key = "YRhveqMv7Hp9GokSXExQwHYlKFkSrDLLFdgx8DSI"
server_url = "https://api.upbit.com"


payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
    'Authorization': authorization,
    "accept": "application/json"
}

resAPIKeys = requests.get(server_url + '/v1/api_keys', headers=headers)
resWallet = requests.get(server_url + '/v1/status/wallet', headers=headers)

print(resWallet.json())
print(resAPIKeys.json())
