def get_top_artists(client, limit, time_range):
    response = client.current_user_top_artists(limit=limit, time_range=time_range)
    items = response.get("items")
    top_artists = [item["name"] for item in items]
    return top_artists

def get_top_tracks(client, limit, time_range):
    response = client.current_user_top_tracks(limit=limit, time_range=time_range)
    items = response.get("items")
    top_tracks = [item["name"] for item in items]
    return top_tracks