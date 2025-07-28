# 📺 YouTube Video Recommendation System

## 🚀 Project Overview

This project aims to build a **YouTube-style video recommendation system** using metadata collected via the **YouTube Data API**. It clusters similar videos based on tags and descriptions and recommends content through an interactive **Streamlit web app**. The system is integrated with **AWS** for data storage and deployment.

---

## 🎯 Goals

- Collect and store YouTube video data via API.
- Preprocess and clean the collected metadata.
- Cluster videos using machine learning (KMeans).
- Build a web application with Streamlit for live recommendations.
- Deploy on AWS (EC2 for app, S3 for raw data, RDS for structured data).

---

## 🧠 Use Cases

- 🔍 **Content Discovery**: Help users find related videos quickly.
- 📊 **Targeted Marketing**: Recommend clusters for ad placement.
- 📌 **Content Categorization**: Group videos for content curators.
- 📈 **User Engagement**: Increase time spent through recommendations.

---

## ⚙️ Tech Stack

| Area                  | Tools/Tech                              |
|-----------------------|------------------------------------------|
| Language              | Python                                   |
| Data API              | YouTube Data API v3                      |
| Data Storage          | AWS S3, AWS RDS                          |
| Clustering Algorithm  | KMeans (Scikit-learn)                    |
| Web Framework         | Streamlit                                |
| Deployment            | AWS EC2                                  |
| Database ORM          | SQLAlchemy (for RDS)                     |
| Environment Variables | python-dotenv / .env                     |

---
---

### ✅ Results

- Successfully collected and stored metadata for YouTube videos from selected channels using the YouTube Data API.
- Cleaned and structured raw JSON data, then stored it in AWS RDS for efficient querying.
- Applied clustering algorithms (e.g., KMeans) to group videos based on tags and content features.
- Developed a Streamlit web application to allow users to search videos and receive related content recommendations.
- Achieved a Silhouette Score above 0.5, indicating reasonably well-separated clusters.
- Deployed the Streamlit application on AWS EC2 for real-time access.

---

### 🔍 Conclusion

This project successfully demonstrates an end-to-end YouTube video recommendation system that integrates data collection, preprocessing, unsupervised learning, and deployment. By clustering videos based on metadata (especially tags and descriptions), users can easily discover related content without relying on traditional collaborative filtering. The pipeline showcases practical skills in working with APIs, cloud storage (AWS), machine learning, and web application development.

---

### 🚧 Future Improvements

- **Semantic Embeddings**: Use models like BERT or Sentence Transformers to capture deeper meaning from descriptions and tags.
- **Hybrid Recommendations**: Combine clustering with user behavior data for a hybrid model (content + collaborative).
- **Automated Data Refresh**: Schedule regular updates using CRON jobs or AWS Lambda.
- **Ranking Mechanism**: Prioritize recommended videos using popularity metrics like views and likes.
- **UI Enhancements**: Make the interface more dynamic and user-friendly, similar to YouTube’s native experience.
- **Feedback Loop**: Integrate user feedback to refine recommendations over time.
- **Docker & CI/CD**: Containerize the app and automate deployment for production use.

---

