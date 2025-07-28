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
