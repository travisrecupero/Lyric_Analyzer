# Lyric_Analyzer

Takes in an artist/song and outputs its "meaning".

## Files Included:

- **artist.py**
  - Class to store `artist_id` of desired artists.

- **config.py**
  - Contains API keys required for the project:
    - `genius_rapid_api_key`: [Get from RapidAPI - Genius Song Lyrics API](https://rapidapi.com/Glavier/api/genius-song-lyrics1/)
    - `genius_api_key`: [Get from Genius API](https://genius.com/signup_or_login)
    - `topic_tagging_api_key`: [Get from RapidAPI - Topic Tagging API](https://rapidapi.com/twinword/api/topic-tagging/)

- **data.json**
  - An example JSON file representing the response from the Genius API.

- **main.py**
  - Imports necessary modules and performs the following actions:
    - Fetches song lyrics and metadata using the Genius API.
    - Retrieves the meaning of lyrics through the Topic Tagging API.
    - Processes and prints lyrics after removing unnecessary text.
    - Allows querying for an artist and song to display lyrics and their meaning.

## Instructions / Usage

1. Configuration:

    - Obtain API keys and fill in the respective fields in `config.py`.
    - Replace `genius_rapid_api_key`, `genius_api_key`, and `topic_tagging_api_key` with your valid keys.

2. Open your terminal.

3. Navigate to the project directory.

4. Run the following command:

    ```bash
    python main.py
    ```

## Output
Example of program running using 1979 by The Smashing Pumpkins:
```

Enter artist name:The Smashing Pumpkins
Enter a song name:1979
Searching for "1979" by The Smashing Pumpkins...
Done.

Shakedown 1979
Cool kids never have the time
On a live wire right up off the street 
You and I should meet
Junebug skippin' like a stone
With the headlights pointed at the dawn
We were sure we'd never see an end     
To it all
... # rest of lyrics
The street heats the urgency of now
As you see there's no one around.

{"keyword":{"know":4,"just":3,"care":3,"blues":2,"sure":2,"bone":2,"guess":2,"zipper":2,"shake":2,"forget":2},"topic":{"mind":0.15381301163291683,"future":0.11963234238115754,"house":0.11963234238115754,"run":0.11963234238115754,"feel":0.11963234238115754,"period":0.11963234238115754,"machine":0.1025420077552779,"water":0.1025420077552779,"time":0.1025420077552779,"power":0.1025420077552779},"version":"7.0.7","author":"twinword inc.","email":"help@twinword.com","result_code":"200","result_msg":"Success"}

```
