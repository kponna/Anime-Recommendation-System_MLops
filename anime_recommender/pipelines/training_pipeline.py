import sys
from anime_recommender.loggers.logging import logging
from anime_recommender.exception.exception import AnimeRecommendorException

from anime_recommender.components.data_ingestion import DataIngestion
from anime_recommender.components.data_transformation import DataTransformation
from anime_recommender.components.collaborative_recommender import CollaborativeModelTrainer
from anime_recommender.components.content_based_recommender import ContentBasedModelTrainer
from anime_recommender.components.top_anime_recommenders import PopularityBasedRecommendor
from anime_recommender.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataTransformationConfig,
    CollaborativeModelConfig,
    ContentBasedModelConfig,
)
from anime_recommender.entity.artifact_entity import (
    DataIngestionArtifact,
    DataTransformationArtifact,
    CollaborativeModelArtifact,
    ContentBasedModelArtifact,
)

class TrainingPipeline:
    """
    Orchestrates the entire anime recommender training pipeline, including
    data ingestion, transformation, model training, and popularity-based recommendations.
    """
    def __init__(self):
        """
        Initialize the TrainingPipeline with required configurations.
        """
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Starts the data ingestion process.
        Returns:
            DataIngestionArtifact: Contains information about ingested data.
        """
        try:
            logging.info("Initiating Data Ingestion...")
            data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.ingest_data()
            logging.info(f"Data Ingestion completed.")
            return data_ingestion_artifact
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataTransformationArtifact:
        """
        Starts the data transformation process.
        Returns:
            DataTransformationArtifact: Contains transformed data.
        """
        try:
            logging.info("Initiating Data Transformation...")
            data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
            data_transformation = DataTransformation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_transformation_config=data_transformation_config
            )
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info(f"Data Transformation completed.")
            return data_transformation_artifact
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

    def start_collaborative_model_training(self, data_transformation_artifact: DataTransformationArtifact) -> CollaborativeModelArtifact:
        """
        Starts collaborative filtering model training.
        Returns:
            CollaborativeModelTrainerArtifact: Trained collaborative model artifact.
        """
        try:
            logging.info("Initiating Collaborative Model Training...")
            collaborative_model_config = CollaborativeModelConfig(self.training_pipeline_config)
            collaborative_model_trainer = CollaborativeModelTrainer(
                collaborative_model_trainer_config=collaborative_model_config,
                data_transformation_artifact=data_transformation_artifact
            )
            collaborative_model_trainer_artifact = collaborative_model_trainer.initiate_model_trainer(model_type='user_knn')
            logging.info(f"Collaborative Model Training completed: {collaborative_model_trainer_artifact}")
            return collaborative_model_trainer_artifact
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

    def start_content_based_model_training(self, data_ingestion_artifact: DataIngestionArtifact) -> ContentBasedModelArtifact:
        """
        Starts content-based filtering model training.
        Returns:
            ContentBasedModelTrainerArtifact: Trained content-based model artifact.
        """
        try:
            logging.info("Initiating Content-Based Model Training...")
            content_based_model_config = ContentBasedModelConfig(self.training_pipeline_config)
            content_based_model_trainer = ContentBasedModelTrainer(
                content_based_model_trainer_config=content_based_model_config,
                data_ingestion_artifact=data_ingestion_artifact
            )
            content_based_model_trainer_artifact = content_based_model_trainer.initiate_model_trainer()
            logging.info(f"Content-Based Model Training completed: {content_based_model_trainer_artifact}")
            return content_based_model_trainer_artifact
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

    def start_popularity_based_filtering(self, data_ingestion_artifact: DataIngestionArtifact):
        """
        Generates popularity-based recommendations.
        """
        try:
            logging.info("Initiating Popularity-Based Filtering...")
            filtering = PopularityBasedRecommendor(data_ingestion_artifact=data_ingestion_artifact)
            recommendations = filtering.initiate_model_trainer(filter_type='popular_animes')
            logging.info("Popularity-Based Filtering completed.")
            return recommendations
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

    def run_pipeline(self):
        """
        Executes the entire training pipeline.
        """
        try:
            # Data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()

            # Data Transformation
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact)

            # Collaborative Model Training
            collaborative_model_trainer_artifact = self.start_collaborative_model_training(data_transformation_artifact)

            # Content-Based Model Training
            content_based_model_trainer_artifact = self.start_content_based_model_training(data_ingestion_artifact)

            # Popularity-Based Filtering
            popularity_recommendations = self.start_popularity_based_filtering(data_ingestion_artifact)

            logging.info("Training Pipeline executed successfully.")
        except Exception as e:
            raise AnimeRecommendorException(e, sys)