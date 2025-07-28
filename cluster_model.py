import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def cluster_videos(df):
    df['tag_str'] = df['tags'].apply(lambda x: ' '.join(x) if isinstance(x, list) else '')
    tfidf = TfidfVectorizer(stop_words='english')
    X = tfidf.fit_transform(df['tag_str'])

    model = KMeans(n_clusters=5, random_state=42)
    df['cluster'] = model.fit_predict(X)
    
    score = silhouette_score(X, df['cluster'])
    print(f"✅ Clustering completed with Silhouette Score: {score:.2f}")
    
    return df, model

if __name__ == "__main__":
    df = pd.read_csv("data/cleaned/cleaned_data.csv")
    clustered_df, model = cluster_videos(df)
    clustered_df.to_csv("data/cleaned/clustered_data.csv", index=False)
