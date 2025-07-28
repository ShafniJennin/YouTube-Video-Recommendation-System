import os
import json
import requests
from googleapiclient.discovery import build

API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_channel_videos(channel_id):
    res = youtube.channels().list(id=channel_id, part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page = None

    while True:
        res = youtube.playlistItems().list(
            playlistId=playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page
        ).execute()

        for item in res['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_data = youtube.videos().list(
                id=video_id,
                part='snippet,statistics'
            ).execute()
            videos.append(video_data)

        next_page = res.get('nextPageToken')
        if not next_page:
            break

    return videos

def save_raw_data(data, filename='data/raw/youtube_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    CHANNEL_ID = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Example
    data = get_channel_videos(CHANNEL_ID)
    save_raw_data(data)
    print(f"✅ Collected {len(data)} videos.")
