import sys
from anime_recommender.pipelines.training_pipeline import TrainingPipeline
from anime_recommender.loggers.logging import logging
from anime_recommender.exception.exception import AnimeRecommendorException

if __name__ == "__main__":
    try:
        logging.info("Starting the Anime Recommendation System Training Pipeline...")
        pipeline = TrainingPipeline()
        pipeline.run_pipeline() 
    except Exception as e:
        logging.error(f"Pipeline execution failed: {str(e)}")
        raise AnimeRecommendorException(e, sys)
     



     
# import sys
# from anime_recommender.loggers.logging import logging
# from anime_recommender.exception.exception import AnimeRecommendorException
# from anime_recommender.components.data_ingestion import DataIngestion
# from anime_recommender.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataTransformationConfig,CollaborativeModelConfig,ContentBasedModelConfig
# from anime_recommender.components.data_transformation import DataTransformation
# from anime_recommender.components.collaborative_recommender import CollaborativeModelTrainer
# from anime_recommender.components.content_based_recommender import ContentBasedModelTrainer 
# from anime_recommender.components.top_anime_recommenders import PopularityBasedRecommendor


# if __name__ == "__main__":
#     try:
        # training_pipeline_config = TrainingPipelineConfig()  
        # data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        # data_ingestion = DataIngestion(data_ingestion_config)
        # logging.info("Initiating Data Ingestion.")
        # data_ingestion_artifact = data_ingestion.ingest_data()
        # logging.info(f"Data ingestion completed.")
        # print(data_ingestion_artifact)

        # # Data Transformation
        # data_transformation_config = DataTransformationConfig(training_pipeline_config)
        # data_transformation = DataTransformation(data_ingestion_artifact,data_transformation_config)
        # logging.info("Initiating Data Transformation.")
        # data_transformation_artifact = data_transformation.initiate_data_transformation()
        # logging.info("Data Transformation Completed.")
        # print(data_transformation_artifact)

        # # Collaborative Model Training
        # collaborative_model_trainer_config = CollaborativeModelConfig(training_pipeline_config)
        # collaborative_model_trainer = CollaborativeModelTrainer(collaborative_model_trainer_config= x,data_transformation_artifact=data_transformation_artifact)
        # logging.info("Initiating Collaborative Model training.")
        # collaborative_model_trainer_artifact = collaborative_model_trainer.initiate_model_trainer(model_type='user_knn')
        # logging.info("Collaborative Model training completed.")
        # print(collaborative_model_trainer_artifact)

        # # Content Based Model Training
        # content_based_model_trainer_config = ContentBasedModelConfig(training_pipeline_config)
        # content_based_model_trainer = ContentBasedModelTrainer(content_based_model_trainer_config=content_based_model_trainer_config,data_ingestion_artifact=data_ingestion_artifact)
        # logging.info("Initiating Content Based Model training.")
        # content_based_model_trainer_artifact = content_based_model_trainer.initiate_model_trainer()
        # logging.info("Content Based Model training completed.")
        # print(content_based_model_trainer_artifact)

        # # Popularity Based Filtering
        # logging.info("Initiating Popularity based filtering.")
        # filtering = PopularityBasedRecommendor(data_ingestion_artifact=data_ingestion_artifact)
        # popularity_recommendations = filtering.initiate_model_trainer(filter_type='top_avg_rated')
        # logging.info("Popularity based filtering completed.") 

#     except Exception as e:
#             raise AnimeRecommendorException(e, sys)