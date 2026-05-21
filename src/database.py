import sqlite3

def get_connection():
    con = sqlite3.connect("spotivault.db")
    cur = con.cursor()
    return con, cur

def init_db():
    con, cur = get_connection()
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS artists (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 artist_uri TEXT UNIQUE
                )
            """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS albums (
                id INTEGER PRIMARY KEY,
                name TEXT,
                artist_id INTEGER REFERENCES artists(id),
                UNIQUE(name, artist_id)
                )
            """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS tracks (
                id INTEGER PRIMARY KEY,
                album_id INTEGER REFERENCES albums(id),
                name TEXT,
                track_uri TEXT UNIQUE,
                artist_id INTEGER REFERENCES artists(id)
                )
            """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS plays (
                id INTEGER PRIMARY KEY,
                track_id INTEGER REFERENCES tracks(id),
                skipped BOOLEAN,
                timestamp TEXT UNIQUE,
                ms_played INTEGER
                )
            """)
    
    con.commit()
    con.close()

def save_recently_played(items):
    con, cur = get_connection()
    new_plays = 0

    for item in items:
        artist_name = item["track"]["artists"][0]["name"]
        artist_uri = item["track"]["artists"][0]["uri"]
        album_name = item["track"]["album"]["name"]
        track_name = item["track"]["name"]
        track_uri = item["track"]["uri"]
        timestamp = item["played_at"]
        skipped = None
        

        cur.execute("INSERT OR IGNORE INTO artists (name, artist_uri) VALUES (?, ?)", (artist_name, artist_uri))
        artist_id = cur.execute("SELECT id FROM artists WHERE artist_uri = ?", (artist_uri,)).fetchone()[0]
        cur.execute("INSERT OR IGNORE INTO albums (name, artist_id) VALUES (?, ?)", (album_name, artist_id))
        album_id = cur.execute("SELECT id FROM albums WHERE name = ?", (album_name,)).fetchone()[0]
        cur.execute("INSERT OR IGNORE INTO tracks (name, track_uri, artist_id, album_id) VALUES (?, ?, ?, ?)", (track_name, track_uri, artist_id, album_id))
        track_id = cur.execute("SELECT id FROM tracks WHERE name = ?", (track_name,)).fetchone()[0]
        cur.execute("INSERT OR IGNORE INTO plays (track_id, timestamp, skipped) VALUES (?, ?, ?)", (track_id, timestamp, skipped))
        if cur.rowcount > 0: new_plays += 1

    con.commit()
    print(f"Saved {new_plays} new plays")
    con.close()
