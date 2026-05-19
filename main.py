from src.client import get_client
from src.stats import get_top_artists

client = get_client()
user = client.current_user()

top_artists_short = get_top_artists(client, 5, "short_term")
top_artists_med = get_top_artists(client, 5, "medium_term")
top_artists_long = get_top_artists(client, 5, "long_term")

user_name =  user.get("display_name")
print(user_name)
print(top_artists_short)
print(top_artists_med)
print(top_artists_long)
