import os
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import  cosine_similarity
import joblib


class ContentBasedRecommender:
    """
    A content-based recommender system using TF-IDF Vectorizer and Cosine Similarity.
    """
    def __init__(self, df): 
        try:
            # Drop missing values from the DataFrame
            self.df = df.dropna()
            
            # Create a Series mapping anime names to their indices
            self.indices = pd.Series(self.df.index, index=self.df['name']).drop_duplicates()
            
            # Initialize and fit the TF-IDF Vectorizer on the 'genres' column
            self.tfv = TfidfVectorizer(
                min_df=3,
                strip_accents='unicode',
                analyzer='word',
                token_pattern=r'\w{1,}',
                ngram_range=(1, 3),
                stop_words='english'
            )
            self.tfv_matrix = self.tfv.fit_transform(self.df['genres'])
             
            self.cosine_sim = cosine_similarity(self.tfv_matrix, self.tfv_matrix) 

        except Exception as e:
            raise e
    def save_model(self, model_path):
        """Save the trained model (TF-IDF and Cosine Similarity Matrix) to a file."""
        try:
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            with open(model_path, 'wb') as f:
                joblib.dump((self.tfv, self.cosine_sim), f)
             
        except Exception as e:
            raise e
    def get_rec_cosine(self, title, model_path, n_recommendations=5):
        """Get recommendations based on cosine similarity for a given anime title."""
        try:
            # Load the model (TF-IDF and cosine similarity matrix)
            with open(model_path, 'rb') as f:
                self.tfv, self.cosine_sim = joblib.load(f)

            # Check if the DataFrame is loaded
            if self.df is None:
                raise ValueError("The DataFrame is not loaded, cannot make recommendations.")
            
            if title not in self.indices.index:
                return f"Anime title '{title}' not found in the dataset."
            
            idx = self.indices[title]
            cosinesim_scores = list(enumerate(self.cosine_sim[idx]))
            cosinesim_scores = sorted(cosinesim_scores, key=lambda x: x[1], reverse=True)[1:n_recommendations + 1]
            anime_indices = [i[0] for i in cosinesim_scores]
            
            return pd.DataFrame({
                'Anime name': self.df['name'].iloc[anime_indices].values,
                'Image URL': self.df['image url'].iloc[anime_indices].values,
                'Genres': self.df['genres'].iloc[anime_indices].values,
                'Rating': self.df['average_rating'].iloc[anime_indices].values
            })
        except Exception as e: 
            raise e
        