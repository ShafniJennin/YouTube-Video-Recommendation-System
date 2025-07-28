import pandas as pd
import streamlit as st

df = pd.read_csv("data/cleaned/clustered_data.csv")

st.title("📺 YouTube Video Recommendation System")
query = st.text_input("🔍 Search by keyword:")

if query:
    results = df[df['title'].str.contains(query, case=False, na=False)]
    if not results.empty:
        cluster = results['cluster'].iloc[0]
        recs = df[df['cluster'] == cluster].sample(5)
        st.subheader("📢 Recommendations:")
        for _, row in recs.iterrows():
            st.markdown(f"**{row['title']}**  \nViews: {row['views']} | Likes: {row['likes']}  \n")
    else:
        st.warning("No videos found.")
