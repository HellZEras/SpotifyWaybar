import spotipy
import spotipy.util as util
import os
import json
import psutil

CLIENT_ID = "replace with ur client id"
redirect_uri = "replace with ur redirect uri"
CLIENT_SECRET = "replace with ur client secret key" 
username = "replace with ur username"
scope = "user-read-currently-playing"
token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)
sp = spotipy.Spotify(auth=token)
var = False
data = {}
def is_process_running(name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == name:
            return "Spotify Online"
    return "Spotify Offline"
if is_process_running("spotify") == "Spotify Online":
    data['text'] = "Spotify Online"
    var = True


if var:    
    try:
        currentsong = sp.currently_playing()
        song_name = currentsong['item']['name']
        song_artist = currentsong['item']['artists'][0]['name']
        data['text'] = "🎵 {} by {}".format(song_name, song_artist)
    except Exception:
        data['text'] = "Spotify Online"
else:
    data['text'] = "Spotify Offline"
print(json.dumps(data))

