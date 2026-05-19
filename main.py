from src.client import get_client
from src.stats import get_top_artists, get_top_tracks

client = get_client()
user = client.current_user()

top_artists_short = get_top_artists(client, 5, "short_term")
top_artists_med = get_top_artists(client, 5, "medium_term")
top_artists_long = get_top_artists(client, 5, "long_term")

top_tracks_short = get_top_tracks(client, 5, "short_term")
top_tracks_med = get_top_tracks(client, 5, "medium_term")
top_tracks_long = get_top_tracks(client, 5, "long_term")

user_name =  user.get("display_name")
print(user_name)
print(top_artists_short)
print(top_artists_med)
print(top_artists_long)
print(top_tracks_short)
print(top_tracks_med)
print(top_tracks_long)
