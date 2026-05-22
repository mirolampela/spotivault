from src.client import get_client
from src.stats import get_top_artists, get_top_tracks, get_recently_played
from src.display import print_top_artists
from src.database import init_db, save_recently_played, save_history
from src.importer import import_history, import_all_history
import glob

init_db()

client = get_client()
user = client.current_user()

top_artists_short = get_top_artists(client, 5, "short_term")
top_artists_med = get_top_artists(client, 5, "medium_term")
top_artists_long = get_top_artists(client, 5, "long_term")

top_tracks_short = get_top_tracks(client, 5, "short_term")
top_tracks_med = get_top_tracks(client, 5, "medium_term")
top_tracks_long = get_top_tracks(client, 5, "long_term")

user_name =  user.get("display_name")
rec = get_recently_played(client, 50)

history = import_all_history(r"C:/Users/mirol/Documents/Spotify Extended Streaming History")
save_history(history)
#save_recently_played(rec)
