"""
Defining common constant variables
"""
PIPELINE_NAME: str = "AnimeRecommender"
ARTIFACT_DIR: str = "Artifacts"
ANIME_FILE_NAME: str = "Animes.csv"
RATING_FILE_NAME:str = "UserRatings.csv"
MERGED_FILE_NAME:str = "Anime_UserRatings.csv" 

ANIME_FILE_PATH:str = "krishnaveni76/Animes"
RATING_FILE_PATH:str = "krishnaveni76/UserRatings"
ANIMEUSERRATINGS_FILE_PATH:str = "krishnaveni76/Anime_UserRatings"
MODELS_FILEPATH = "krishnaveni76/anime-recommendation-models"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""  
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

"""
Data Transformation related constant start with DATA_VALIDATION VAR NAME
"""
DATA_TRANSFORMATION_DIR:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str = "transformed" 

"""
Model Trainer related constant start with MODEL TRAINER VAR NAME
""" 
MODEL_TRAINER_DIR_NAME: str = "trained_models"

MODEL_TRAINER_COL_TRAINED_MODEL_DIR: str = "collaborative_recommenders"
MODEL_TRAINER_SVD_TRAINED_MODEL_NAME: str = "svd.pkl"
MODEL_TRAINER_ITEM_KNN_TRAINED_MODEL_NAME: str = "itembasedknn.pkl"
MODEL_TRAINER_USER_KNN_TRAINED_MODEL_NAME: str = "userbasedknn.pkl"

MODEL_TRAINER_CON_TRAINED_MODEL_DIR:str = "content_based_recommenders"
MODEL_TRAINER_COSINESIMILARITY_MODEL_NAME:str = "cosine_similarity.pkl"