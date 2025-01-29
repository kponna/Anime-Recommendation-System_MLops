import sys
import numpy as np
import pandas as pd  
from anime_recommender.exception.exception import AnimeRecommendorException

class PopularityBasedFiltering:
    def __init__(self, df):
        try:
            self.df = df
            self.df['average_rating'] = pd.to_numeric(self.df['average_rating'], errors='coerce')
            self.df['average_rating'].fillna(self.df['average_rating'].median())
        except Exception as e:
            raise AnimeRecommendorException(e, sys)
         
    def popular_animes(self, n=10):
        sorted_df = self.df.sort_values(by=['popularity'], ascending=True)
        top_n_anime = sorted_df.head(n)
        return pd.DataFrame({
            'Anime name': top_n_anime['name'].values,
            'Image URL': top_n_anime['image url'].values,
            'Genres': top_n_anime['genres'].values,
            'Rating': top_n_anime['average_rating'].values
        })
      
    def top_ranked_animes(self, n=10):
        self.df['rank'] = self.df['rank'].replace('UNKNOWN', np.nan).astype(float)
        df_filtered = self.df[self.df['rank'] > 1]
        sorted_df = df_filtered.sort_values(by=['rank'], ascending=True)
        top_n_anime = sorted_df.head(n)
        return pd.DataFrame({
            'Anime name': top_n_anime['name'].values,
            'Image URL': top_n_anime['image url'].values,
            'Genres': top_n_anime['genres'].values,
            'Rating': top_n_anime['average_rating'].values
        }) 
    
    def overall_top_rated_animes(self, n=10):
        sorted_df = self.df.sort_values(by=['average_rating'], ascending=False)
        top_n_anime = sorted_df.head(n)
        return pd.DataFrame({
            'Anime name': top_n_anime['name'].values,
            'Image URL': top_n_anime['image url'].values,
            'Genres': top_n_anime['genres'].values,
            'Rating': top_n_anime['average_rating'].values
        }) 
    
    def favorite_animes(self, n=10):
        sorted_df = self.df.sort_values(by=['favorites'], ascending=False)
        top_n_anime = sorted_df.head(n)
        return pd.DataFrame({
            'Anime name': top_n_anime['name'].values,
            'Image URL': top_n_anime['image url'].values,
            'Genres': top_n_anime['genres'].values,
            'Rating': top_n_anime['average_rating'].values
        }) 
    
    def top_animes_members(self, n=10):
        sorted_df = self.df.sort_values(by=['members'], ascending=False)
        top_n_anime = sorted_df.head(n)
        return pd.DataFrame({
            'Anime name': top_n_anime['name'].values,
            'Image URL': top_n_anime['image url'].values,
            'Genres': top_n_anime['genres'].values,
            'Rating': top_n_anime['average_rating'].values
        })
    
    def popular_anime_among_members(self, n=10):
        sorted_df = self.df.sort_values(by=['members', 'average_rating'], ascending=[False, False]).drop_duplicates(subset='name')['name']
        popular_animes = sorted_df.head(n)
        return pd.DataFrame({
            'Anime name': popular_animes['name'].values,
            'Image URL': popular_animes['image url'].values,
            'Genres': popular_animes['genres'].values,
            'Rating': popular_animes['average_rating'].values
        })
    
    def top_avg_rated(self, n=10): 
        self.df['average_rating'] = pd.to_numeric(self.df['average_rating'], errors='coerce')
        
        # Replace NaN values with the median
        median_rating = self.df['average_rating'].median()
        self.df['average_rating'].fillna(median_rating)
        # Select top N animes by average rating
        top_animes = (
            self.df.drop_duplicates(subset='name')
                    .nlargest(n, 'average_rating')[['name', 'average_rating', 'image url', 'genres']]
        )
        return pd.DataFrame({
            'Anime name': top_animes['name'].values,
            'Image URL': top_animes['image url'].values,
            'Genres': top_animes['genres'].values,
            'Rating': top_animes['average_rating'].values
        })