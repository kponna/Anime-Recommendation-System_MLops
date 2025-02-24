import os
from datetime import datetime
from anime_recommender.constant import *

class TrainingPipelineConfig:
    """
    Configuration for the training pipeline, including artifact directory and timestamp.
    """
    def __init__(self, timestamp=datetime.now()):
        """
        Initialize the configuration with a unique timestamp.
        """
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = PIPELINE_NAME
        self.artifact_dir = os.path.join(ARTIFACT_DIR, timestamp)
        self.timestamp: str = timestamp
    

class DataIngestionConfig:
    """
    Configuration for data ingestion, including paths for feature store.
    """
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        """
        Initialize data ingestion paths.
        """
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
        self.feature_store_anime_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, ANIME_FILE_NAME) 
        self.feature_store_userrating_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, RATING_FILE_NAME)
        self.anime_filepath: str = ANIME_FILE_PATH
        self.rating_filepath: str = RATING_FILE_PATH 

class DataTransformationConfig:
    """
    Configuration for data transformation, including paths for transformed data.
    """
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        """
        Initialize data transformation paths.
        """
        self.data_transformation_dir:str = os.path.join(training_pipeline_config.artifact_dir,DATA_TRANSFORMATION_DIR)
        self.merged_file_path:str = os.path.join(self.data_transformation_dir,DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,MERGED_FILE_NAME)

class CollaborativeModelConfig:
    """
    Configuration for model training, including paths for trained models.
    """
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        """
        Initialize model trainer paths.
        """
        self.model_trainer_dir:str = os.path.join(training_pipeline_config.artifact_dir,MODEL_TRAINER_DIR_NAME)
        self.svd_trained_model_file_path:str = os.path.join(self.model_trainer_dir,MODEL_TRAINER_COL_TRAINED_MODEL_DIR,MODEL_TRAINER_SVD_TRAINED_MODEL_NAME)
        self.user_knn_trained_model_file_path:str = os.path.join(self.model_trainer_dir,MODEL_TRAINER_COL_TRAINED_MODEL_DIR,MODEL_TRAINER_USER_KNN_TRAINED_MODEL_NAME)
        self.item_knn_trained_model_file_path:str = os.path.join(self.model_trainer_dir,MODEL_TRAINER_COL_TRAINED_MODEL_DIR,MODEL_TRAINER_ITEM_KNN_TRAINED_MODEL_NAME)
      
class ContentBasedModelConfig:
    """
    Configuration for model training, including paths for trained models.
    """
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        """
        Initialize model trainer paths.
        """
        self.model_trainer_dir:str = os.path.join(training_pipeline_config.artifact_dir,MODEL_TRAINER_DIR_NAME)
        self.cosine_similarity_model_file_path:str = os.path.join(self.model_trainer_dir,MODEL_TRAINER_CON_TRAINED_MODEL_DIR,MODEL_TRAINER_COSINESIMILARITY_MODEL_NAME)