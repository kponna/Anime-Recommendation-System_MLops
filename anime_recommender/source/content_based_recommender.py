import sys
from anime_recommender.loggers.logging import logging
from anime_recommender.exception.exception import AnimeRecommendorException
from anime_recommender.entity.config_entity import ContentBasedModelConfig
from anime_recommender.entity.artifact_entity import ContentBasedModelArtifact, DataIngestionArtifact
from anime_recommender.utils.main_utils.utils import load_csv_data
from anime_recommender.model_trainer.content_based_modelling import ContentBasedRecommender
from anime_recommender.constant import *
 
class ContentBasedModelTrainer:
    """Class to train the model, track metrics, and save the trained model."""

    def __init__(self, content_based_model_trainer_config: ContentBasedModelConfig, data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.content_based_model_trainer_config = content_based_model_trainer_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

    def initiate_model_trainer(self) -> ContentBasedModelArtifact:
        try:
            logging.info("Loading ingested data...")
            df = load_csv_data(self.data_ingestion_artifact.feature_store_anime_file_path)
            logging.info("Training ContentBasedRecommender model...")
            
            # Initialize and train the model
            recommender = ContentBasedRecommender(df=df )
            
            # Save the model (TF-IDF and cosine similarity matrix)
            recommender.save_model(self.content_based_model_trainer_config.cosine_similarity_model_file_path)
            logging.info("Model saved successfully.")
            
            logging.info("Loading saved model to get recommendations...")
            cosine_recommendations = recommender.get_rec_cosine(title="One Piece", model_path=self.content_based_model_trainer_config.cosine_similarity_model_file_path, n_recommendations=10)
            logging.info(f"Cosine similarity recommendations: {cosine_recommendations}")
            
            # Return artifact with saved model path
            content_model_trainer_artifact = ContentBasedModelArtifact(
                cosine_similarity_model_file_path=self.content_based_model_trainer_config.cosine_similarity_model_file_path
            )
            return content_model_trainer_artifact
        except Exception as e:
            raise AnimeRecommendorException(f"Error in ContentBasedModelTrainer: {str(e)}", sys)