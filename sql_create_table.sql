CREATE TABLE youtube_videos (
    video_id TEXT PRIMARY KEY,
    title TEXT,
    description TEXT,
    tags TEXT,
    publishedAt TIMESTAMP,
    views INTEGER,
    likes INTEGER,
    comments INTEGER,
    cluster INTEGER
);
