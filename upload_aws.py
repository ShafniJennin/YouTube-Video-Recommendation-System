import boto3
import pandas as pd
from sqlalchemy import create_engine

# S3 Upload
def upload_to_s3(file_path, bucket_name, s3_file):
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, s3_file)
    print(f"✅ Uploaded to S3: {s3_file}")

# Upload to RDS
def upload_to_rds(df, db_url, table_name):
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"✅ Uploaded to RDS: {table_name}")

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned/clustered_data.csv")
    upload_to_s3("data/cleaned/clustered_data.csv", "your-bucket", "youtube/clustered_data.csv")

    db_url = "postgresql://user:pass@your-db-endpoint/dbname"
    upload_to_rds(df, db_url, "youtube_videos")
