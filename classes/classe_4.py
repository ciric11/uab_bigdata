import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import glob
import json
import pandas as pd
api_client_id = "41a11a24c118434a8654a7552a23538b"
api_client_secret = "c9214ce7a837422f8335d101a23b91da"

#playlist: hhtps://open.spotify.com/playlist/3oHP7U2qwPVPPE5rbE6PfT
#playlist -100: https://open.spotify.com/playlist/3oopyXIZGLFtHjFYN9KbuI

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

playlist_list= ["3oHP7U2qwPVPPE5rbE6PfT","3oopyXIZGLFtHjFYN9KbuI","4h9dvquufDVDyGuYRHeu73"]
def get_playlist(playlist,offset):
    resposta = spotify.playlist_items(playlist, offset=offset)
    with open(f'{playlist}-{offset}.json', 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent= 4)
    if resposta ["next"] == None:
        print("Final")
        pass
    else:
        offset = offset+100
        print("nova petició")
        get_playlist(playlist,offset)

for playlist in playlist_list:
    offset = 0
    get_playlist(playlist,offset)

files = glob.glob("*.json")
list_tracks = []

for file in files:
    with open(file) as f:
        d = json.load(f)
        tracks = d ["items"]
        for track in tracks:
            track_dict = {}
            track_dict["name"] = track["track"]["name"]
            track_dict ["artist_name"] = track["track"]["artists"][0]["name"]
            track_dict ["duracio_ms"] = track["track"]["duration_ms"]
            track_dict ["duracio_min"] = round(track["track"]["duration_ms"]/1000/60, 2)

            list_tracks.append(track_dict)

df = pd.DataFrame.from_dict(list_tracks)

df.to_csv("output.csv", index=False, sep=";")
