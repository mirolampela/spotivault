import os, spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


# Function for authentication
def get_client():
    load_dotenv()
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    client_rd_uri = os.getenv("SPOTIFY_REDIRECT_URI")
    scope = "user-read-private user-top-read"
    auth = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=client_rd_uri,
        scope=scope
    )
    sp = spotipy.Spotify(auth_manager=auth)

    return sp

