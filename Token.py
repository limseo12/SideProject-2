def search(token):
    endpoint = "https://api.spotify.com/v1/search"

    headers = {"Authorization": "Bearer {}".format(token)}
    query_params = {'q':'BTS','type':'album','limit':5}

    r=requests.get(endpoint,params=query_params,headers)
    print(json.loads(r.text))

