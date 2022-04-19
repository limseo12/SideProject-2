if search_r.status_code!=200:
    logging.error(json.loads(search_r.text))
    if search_r.status_code == 429: #too much request
        retry_afer = json.loads(search_r.headers)['retry-After']
        time.sleep(int(retry_afer))
        search_r=requests.get(endpoint,params=query_params,headers=headers)
    elif search_r.code==401:
        headers = get_token(client_id,client_secret)
        search_r=requests.get(endpoint,params=query_params,headers=headers)
    else:
        logging.error(json.loads(search_r.text))    