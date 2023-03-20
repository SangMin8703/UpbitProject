import requests

url = "https://api.upbit.com/v1/api_keys"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
