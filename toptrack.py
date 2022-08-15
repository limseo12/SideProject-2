from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import sys
import requests
import base64
import json
import logging

# 아래 세줄의 코드가 없으면 이 전체 코드의 실행결과 시
# UnicodeEncodeError: 'cp949' codec can't encode character '\u2013' in position 33:
# illegal multibyte sequence 애러발생하기 때문에 추가한 것임
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


client_id = "2c2a840de60f49ec9bf32be6c1c80f1c"
client_secret = "21a4860c982c4064815955859b6d536a"
##몽고db저장용
toptrack_results = []
def main():
    headers = get_headers(client_id, client_secret)

    try:
        uri = 'spotify:artist:6VuMaDnrHyPL1p4EHjYLi7'

        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        results = sp.artist_top_tracks(uri)
        
        
        # get top 10 tracks
        for track in results['tracks'][:10]:

            toptrack_results.append(track['name'])
            toptrack_results.append(track['preview_url'])
            toptrack_results.append(track['album']['images'][0]['url'])
            print('track    : ' + track['name'])
            print('audio    : ' + track['preview_url'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print()

        print(toptrack_results)

    except:
        ## 애러메세지를 로깅처리
        logging.error(r.text)

        if r.status_code != 403:
            logging.error(r.text)

            ## 사용자 차원에서 해결할 수 있는 애러일 경우
            ## 429 애러는 too many requests일 경우 발생
            if r.status_code == 429:

                retry_after = json.loads(r.headers)['Retry-After']
                time.sleep(int(retry_after))

                r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)

            ## 401 애러는 Authorization에 문제가 있을때 발생하며 대부분은 Access token이 만료가 된 경우
            elif r.status_code == 401:

                headers = get_headers(client_id, client_secret)
                r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)

            ## 사용자 차원에서 해결할 수 없는 애러일 경우
            else:
                sys.exit(1)

    return None


def get_headers(client_id, client_secret):

    endpoint = "https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

    headers = {"Authorization": "Basic {}".format(encoded)}

    payload = {"grant_type": "client_credentials"}

    r = requests.post(endpoint, data=payload, headers=headers)

    access_token = json.loads(r.text)['access_token']

    headers = {"Authorization": "Bearer {}".format(access_token)}

    return headers



##toptrack. py만 실행
if __name__=='__main__':
    main()
