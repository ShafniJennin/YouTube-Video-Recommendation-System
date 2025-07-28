import json
import pandas as pd
import re

def load_raw_data(path='data/raw/youtube_data.json'):
    with open(path, 'r') as f:
        return json.load(f)

def clean_video_data(raw):
    videos = []

    for block in raw:
        for item in block.get('items', []):
            snippet = item['snippet']
            stats = item['statistics']

            videos.append({
                'video_id': item['id'],
                'title': snippet.get('title'),
                'description': snippet.get('description'),
                'tags': snippet.get('tags', []),
                'publishedAt': snippet.get('publishedAt'),
                'views': int(stats.get('viewCount', 0)),
                'likes': int(stats.get('likeCount', 0)),
                'comments': int(stats.get('commentCount', 0))
            })

    return pd.DataFrame(videos)

if __name__ == "__main__":
    raw_data = load_raw_data()
    df = clean_video_data(raw_data)
    df.to_csv("data/cleaned/cleaned_data.csv", index=False)
    print("✅ Cleaned data saved.")
