import json, glob

def import_history(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        tracks = [item for item in data if item["master_metadata_track_name"] is not None]
    
    return tracks

def import_all_history(folder_path):
    files = glob.glob(folder_path + "/Streaming_History_Audio_*.json")
    all_tracks = []
    for file in files:
        tracks = import_history(file)
        all_tracks.extend(tracks)
    return all_tracks