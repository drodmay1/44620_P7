import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="97b28f26f7464badbd313a605af20d11",
        client_secret="e0aa8f8732b347b9a5e69041306d0e41",
        redirect_uri="http://localhost:8888/callback",
        scope="user-library-read"
    ))
    return sp
