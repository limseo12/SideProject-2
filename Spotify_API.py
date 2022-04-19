import requests
import base64
import json

client_id = "2c2a840de60f49ec9bf32be6c1c80f1c"
client_secret = "21a4860c982c4064815955859b6d536a"
endpoint = "https://accounts.spotify.com/apitoken"

encoded = base64.b64encode("{}:{}",format(client_id, client_secret).encode('utf-8')).decode('ascii')

headers = {"Authorization": "Basic {}".format(encoded)}
payload = {"grant_type": "client_credentials"}

response = requests.post(endpoint, data=payload , headers=headers)
access_token = json.loads(response.text)['access_token']

#참고
print(json.loads(response.text))
{'access_token': 'BQ-----', 'token_type': 'Bearer', 'expires_in': 3600}

