import os
import sys
import pandas as pd
from datasets import load_dataset
from anime_recommender.loggers.logging import logging
from anime_recommender.exception.exception import AnimeRecommendorException
from anime_recommender.entity.config_entity import DataIngestionConfig
from anime_recommender.entity.artifact_entity import DataIngestionArtifact
from anime_recommender.utils.main_utils.utils import export_data_to_dataframe

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

    def fetch_data_from_huggingface(self, dataset_path: str, split: str = None) -> pd.DataFrame:
        try:
            logging.info(f"Fetching data from Hugging Face dataset: {dataset_path}")
            # Load dataset from Hugging Face
            dataset = load_dataset(dataset_path, split=split)

            # Convert dataset to pandas DataFrame
            df = pd.DataFrame(dataset['train'])

            # Log some information about the data
            logging.info(f"Shape of the dataframe: {df.shape}")
            logging.info(f"Column names: {df.columns}")
            logging.info(f"Preview of the DataFrame:\n{df.head()}")
            logging.info("Data fetched successfully from Hugging Face.")
            
            return df

        except Exception as e:
            logging.error(f"An error occurred while fetching data: {str(e)}")
            raise AnimeRecommendorException(e, sys)

    def ingest_data(self) -> DataIngestionArtifact:
        try:
            # Load anime and rating data from Hugging Face datasets
            anime_df = self.fetch_data_from_huggingface(self.data_ingestion_config.anime_filepath)
            rating_df = self.fetch_data_from_huggingface(self.data_ingestion_config.rating_filepath)

            # Export data to DataFrame
            export_data_to_dataframe(anime_df, file_path=self.data_ingestion_config.feature_store_anime_file_path)
            export_data_to_dataframe(rating_df, file_path=self.data_ingestion_config.feature_store_userrating_file_path)

            # Create artifact to store data ingestion info
            dataingestionartifact = DataIngestionArtifact(
                feature_store_anime_file_path=self.data_ingestion_config.feature_store_anime_file_path,
                feature_store_userrating_file_path=self.data_ingestion_config.feature_store_userrating_file_path
            )

            return dataingestionartifact

        except Exception as e:
            raise AnimeRecommendorException(e, sys)
