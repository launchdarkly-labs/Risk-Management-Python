import json
import sqlite3
import os
from dotenv import load_dotenv
import ldclient
from ldclient.config import Config

load_dotenv()

## Initialize LaunchDarkly client using the SDK key from your .env file

ld_sdk_key = os.getenv('LD_SDK_KEY')
ld_client = ldclient.set_config(Config(ld_sdk_key))

## Load tracklist from your JSON file
with open('dj_toggles_top_30.json', 'r') as file:
    tracklist = json.load(file)

## Set up SQLite database
def create_database():
    conn = sqlite3.connect('tracklist.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tracks
                 (track_name TEXT, track_length TEXT, artist TEXT, album_name TEXT, track_number INTEGER, release_date TEXT)''')
    for track in tracklist:
        c.execute("INSERT INTO tracks VALUES (?, ?, ?, ?, ?, ?)", 
                  (track['track_name'], track['track_length'], track['artist'], track['album_name'], track['track_number'], track['release_date']))
    conn.commit()
    conn.close()

create_database()

## Get tracks from the JSON and database

def get_tracks_from_json():
    return [track['track_name'] for track in tracklist[:10]]

def get_tracks_from_db():
    conn = sqlite3.connect('tracklist.db')
    c = conn.cursor()
    c.execute("SELECT track_name FROM tracks LIMIT 10")
    tracks = [row[0] for row in c.fetchall()]
    conn.close()
    return tracks

## Main app logic, note how there is two different versions, a usse database version and use JSON version.  

def run_app():
    user = {"key": "user-key-123", "custom": {"groups": ["beta_testers"]}}
    use_database = ld_client.variation("use-database", user, False)

    if use_database:
        print("Using database version")
        tracks = get_tracks_from_db()
    else:
        print("Using JSON version")
        tracks = get_tracks_from_json()

    print("Top 10 Tracks:")
    for i, track in enumerate(tracks, 1):
        print(f"{i}. {track}")

## run the application and close the client
if __name__ == "__main__":
    run_app()
    ld_client.close()