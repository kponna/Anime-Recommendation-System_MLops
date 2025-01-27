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
        self.model_dir=os.path.join("final_model")
        self.timestamp: str = timestamp

class DataIngestionConfig:
    """
    Configuration for data ingestion, including paths for feature store, train, test, and validation files.
    """
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        """
        Initialize data ingestion paths and parameters.
        """
        self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
        self.feature_store_anime_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, ANIME_FILE_NAME) 
        self.feature_store_userrating_file_path: str = os.path.join(self.data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, RATING_FILE_NAME)
        self.anime_filepath: str = ANIME_FILE_PATH
        self.rating_filepath: str = RATING_FILE_PATH 
