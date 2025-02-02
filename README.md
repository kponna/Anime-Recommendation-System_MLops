# Anime Recommendation System

This is an **Anime Recommendation System** that combines multiple recommendation techniques such as **Collaborative Filtering**, **Content-Based Filtering**, and **Popularity-Based Filtering**. The system is designed to continuously ingest and transform data and is **dockerized** for easier deployment. Additionally, **GitHub Actions** is used for **Continuous Integration/Continuous Deployment (CI/CD)** of the **Streamlit** app that serves the recommendations. 
The system provides **personalized anime recommendations** based on user preferences and anime features.  
 
## 🚀 Technologies Used

- **Python**: Main programming language used for building recommendation algorithms and Streamlit app.
- **Docker**: Containerizes the application to ensure a consistent environment across different platforms.
- **Streamlit**: For building and deploying the web app that serves the recommendations.
- **GitHub Actions**: For Continuous Integration and Continuous Deployment (CI/CD) of the application. 
- **Hugging Face**: The datasets and pretrained models used for getting  recommendations is ingested from Hugging Face, ensuring access to high-quality.

## Pipeline Overview  
The pipeline follows a structured sequence of steps to build an **Anime Recommendation System**, including data ingestion, transformation, and multiple recommendation models.

### 1. Data Ingestion 📥  
- Initiates the **data ingestion process**, where anime data is loaded from Hugging Face datasets.  
- The ingested data is saved as artifacts in local folder for further processing.

### 2. Data Transformation 🔄  
- Cleans, transforms and processes the raw data into a structured format.  
- Extracts important features required for **Content-Based Filtering** and prepares data for **Collaborative Filtering**.  

### 3. Collaborative Filtering 🤝  
- Implements **three collaborative filtering models** to recommend anime based on user preferences:  
  - **Singular Value Decomposition (SVD)**: Factorizes the user-item interaction matrix to make personalized recommendations.  
  - **Item-Based K-Nearest Neighbors (Item-KNN)**: Recommends anime similar to a given anime based on user ratings.  
  - **User-Based K-Nearest Neighbors (User-KNN)**: Suggests anime that users with similar preferences have liked.  
- The chosen model is trained using **transformed data**, and the final trained model is stored as an artifact.  
- Once trained, it can generate recommendations for users or anime titles.  

### 4. Content-Based Filtering 🎭  
- Uses extracted anime features like genres to train a **Content-Based Recommendation Model**.  
- This model recommends anime similar to those a user has watched or liked.  
  
### 5. Popularity-Based Filtering ⭐  

This recommendation system ranks anime based on various **popularity metrics**, making it ideal for users who want to discover trending or highly-rated shows **without needing personalized preferences**.  

The system applies different filters to sort anime based on:  

- **Most Popular** 🎭: Anime ranked by **popularity score**, highlighting the most widely recognized titles.  
- **Top Ranked** 🏆: Highest-rated anime, based on **official ranking metrics**.  
- **Overall Top Rated** ⭐: Best-rated anime, sorted by **average user ratings**.  
- **Most Favorited** ❤️: Anime with the highest number of **favorites**, indicating strong fan appreciation.  
- **Highest Member Count** 👥: Anime with the largest **viewer base**, showing widespread appeal.  
- **Popular Among Members** 🔥: Anime with a **high number of members and strong ratings**, making them community favorites.  
- **Highest Average Rating** 🎖️: Shows that have the **best average rating** after handling missing values.   

### Artifacts Storage 📂  
All intermediate and final outputs, including processed datasets and trained models, are first saved locally in the Artifacts folder. These artifacts are then uploaded to Hugging Face for efficient storage and easy access. When building the Streamlit app, these datasets and trained models are retrieved directly from Hugging Face, ensuring seamless integration and scalability.

- The datasets used in this project are available at:  
    - [Anime and User Ratings](https://www.kaggle.com/datasets/krishnaveniponna/anime-and-ratings-list-dataset-2023)  
      
- You can find the Artifacts of trained models here:  
    - [Pre-trained Models](https://huggingface.co/krishnaveni76/anime-recommendation-models)
   
## 🚀 CI/CD Pipeline Integration  

To ensure seamless updates and **automated deployment**, this project utilizes **GitHub Actions** for Continuous Integration and Continuous Deployment (CI/CD). The pipeline is structured as follows:

### 1. **Continuous Integration (CI)**
- **Linting & Code Quality Checks**: The repository is checked for linting errors (currently a placeholder for adding an actual linter).  
- **Unit Testing**: Placeholder for running unit tests to ensure the correctness of the application.  

### 2. **Building & Pushing Docker Image**
- Upon a push to the `main` branch, the pipeline builds a **Docker image** of the Streamlit app.  
- The image is tagged with the latest commit SHA and **pushed to GitHub Container Registry (GHCR)** for versioned storage.  

### 3. **Deployment to Self-Hosted Runner**
- The latest Docker image is **pulled from GHCR** onto a **self-hosted runner**.  
- The previous container instance is stopped and removed to avoid conflicts.  
- A new **Streamlit container** is started with the latest version of the application.  

This **automated CI/CD workflow** ensures that every update to the repository is **validated, built, and deployed** efficiently.  

### Pre-requisites
- Docker
- Hugging face (for datasets and trained models)
- Python 3.8+  
- GitHub Actions setup

### Local step 🔧
1. **Clone the repository**
```bash
   git clone https://github.com/kponna/Anime-Recommendation-System_MLops.git
   cd Anime-Recommendation-System_MLops
``` 
2. **Set Up a Virtual Environment**:
```bash
# For macOS and Linux:
python3 -m venv venv 
# For Windows:
python -m venv venv
``` 
3. **Activate the Virtual Environment**:
```bash
# For macOS and Linux:
source venv/bin/activate 
# For Windows:
.\venv\Scripts\activate
``` 
4. **Install Required Dependencies**:
```bash
pip install -r requirements.txt
```

### Contact 📫
For any questions, suggestions, or collaboration opportunities, feel free to reach out:

📧Email: ponnakrishnaveni76@gmail.com 

🌐 LinkedIn: [Krishnaveni Ponna](https://www.linkedin.com/in/krishnaveni-ponna-28ab93239)

🐦 Twitter: [@Krishnaveni076](https://x.com/Krishnaveni076)