import requests
import json
import config
from artists import Artists
from lyricsgenius import Genius # https://github.com/johnwmillr/LyricsGenius/blob/master/lyricsgenius/genius.py
import re

# Gets meaning of lyrics using topic tagging API
def print_lyrics_meaning(lyrics):
    url = "https://twinword-topic-tagging.p.rapidapi.com/generate/"

    querystring = {"text":lyrics}

    headers = {
        "X-RapidAPI-Key": config.topic_tagging_api_key,
        "X-RapidAPI-Host": "twinword-topic-tagging.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


# Given an artist_id, return response containing 20 songs with metadata
def get_artists_songs(artist_id):
    url = f"https://genius-song-lyrics1.p.rapidapi.com/artists/{artist_id}/songs"

    querystring = {"sort":"title","per_page":"20","page":"1"}

    headers = {
        "X-RapidAPI-Key": config.genius_rapid_api_key,
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    response = requests.get(url, params=querystring, headers=headers)
    
    return response


def remove_lyrics_junk(lyrics):
    # Create pattern to remove
    bracket_pattern = r"\[.*?\]" # anything in between square brackets
    description_pattern = r".*Lyrics" # description in first line
    embed_pattern = r"\d*Embed" # embed tag at end of lyrics

    # Remove any text containing pattern using re.sub
    temp1 = re.sub(bracket_pattern, '', lyrics)
    temp2 = re.sub(description_pattern, '', temp1)
    modified_lyrics = re.sub(embed_pattern, '', temp2)

    return modified_lyrics


# Given a Genius artist_id, write songs by given artist to json
def write_artists_songs_to_json(artist_id):
    artists_songs = get_artists_songs(artist_id).json()
    with open('data.json', 'w') as f:
        f.write(json.dumps(artists_songs))
    
    f = open('data.json')

    data = json.load(f)

    for i in data['response']['songs']:
        print(i['full_title'])


def main():
    # Given a Genius artist_id, write songs by given artist to json
    # write_artists_songs_to_json(artist_id)

    # Query for lyrics, prints lyrics
    genius = Genius(config.genius_api_key)
    artist_query = input("Enter artist name:")
    song_query = input("Enter a song name:")
    song = genius.search_song(title=song_query, artist=artist_query)

    # Store lyrics, remove junk from lyrics (non-text)
    lyrics = str(song.lyrics)
    modified_lyrics = remove_lyrics_junk(lyrics)
    print(modified_lyrics)

    # Get meaning of lyrics
    print_lyrics_meaning(modified_lyrics)

if __name__ == '__main__':
    main()