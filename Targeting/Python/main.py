import json
import sqlite3
import os
import ldclient
from ldclient.config import Config
from ldclient import Context

## Initialize LaunchDarkly client using the SDK key from your .env file

ld_sdk_key = os.environ.get('LD_SDK_KEY')
if not ld_sdk_key:
    raise ValueError("LD_SDK_KEY not found in environment variables")

ldclient.set_config(Config(ld_sdk_key))
ld_client = ldclient.get()

if ld_client.is_initialized():
    print("LaunchDarkly client initialized successfully")
else:
    print("LaunchDarkly client failed to initialize")
    exit(1)

## Load tracklist from your JSON file
with open('dj_toggles_top_songs.json', 'r') as file:
    tracklist = json.load(file)

## Set up SQLite database
def create_database():
    conn = sqlite3.connect('tracklist.db')
    c = conn.cursor()
    
    # Create the table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS tracks
                 (track_name TEXT, track_length TEXT, artist TEXT, album_name TEXT, track_number INTEGER, release_date TEXT)''')
    
    # Remove existing duplicates
    c.execute('''DELETE FROM tracks WHERE rowid NOT IN 
                 (SELECT MIN(rowid) FROM tracks GROUP BY track_name, artist)''')
    
    # Create the unique index
    c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS idx_track_artist 
                 ON tracks(track_name, artist)''')
    
    # Insert new tracks, ignoring duplicates
    for track in tracklist:
        c.execute('''INSERT OR IGNORE INTO tracks 
                     (track_name, track_length, artist, album_name, track_number, release_date)
                     VALUES (?, ?, ?, ?, ?, ?)''', 
                  (track['track_name'], track['track_length'], track['artist'], 
                   track['album_name'], track['track_number'], track['release_date']))
    
    conn.commit()
    conn.close()

create_database()

## Get tracks from the JSON and database

def get_tracks_from_json():
    return [track['track_name'] for track in tracklist[:10]]

def get_tracks_from_db():
    conn = sqlite3.connect('tracklist.db')
    c = conn.cursor()
    c.execute("SELECT track_name FROM tracks")
    tracks = [row[0] for row in c.fetchall()]
    conn.close()
    return tracks

## Main app logic, note how there is two different versions, a use database version and use JSON version.  

from ldclient.context import Context

def run_app():
    dj_toggle_team = Context.builder('dj-toggle-123').set('groups', ['dj_team']).build()
    general_audience = Context.builder('general-456').set('groups', ['general_audience']).build()

    use_database = ld_client.variation("use-database", dj_toggle_team, False)
    show_release_dates = ld_client.variation("show-release-dates", general_audience, False)

    if use_database:
        print("Full playlist for DJ Toggle's team")
        tracks = get_tracks_from_db()
    else:
        print("Top 10 tracks for general audience")
        tracks = get_tracks_from_json()

    print("DJ Toggle's Top Tracks")
    for i, track in enumerate(tracks, 1):
        track_info = f"{i}. {track['track_name']} by {track['artist']}"
        if show_release_dates:
            track_info += f" (Released: {track['release_date']})"
        print(track_info)

## Run the application and close the client
if __name__ == "__main__":
    run_app()
    ld_client.close()
