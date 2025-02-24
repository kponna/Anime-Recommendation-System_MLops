import sys
from anime_recommender.loggers.logging import logging
from anime_recommender.exception.exception import AnimeRecommendorException
from anime_recommender.entity.config_entity import CollaborativeModelConfig
from anime_recommender.entity.artifact_entity import DataTransformationArtifact, CollaborativeModelArtifact
from anime_recommender.utils.main_utils.utils import load_csv_data, save_model, load_object
from anime_recommender.source.collaborative_modelling import CollaborativeAnimeRecommender

class CollaborativeModelTrainer:
    """
    Trains and saves collaborative filtering recommendation models.

    This class supports three types of models:
    - Singular Value Decomposition (SVD)
    - Item-based K-Nearest Neighbors (KNN)
    - User-based K-Nearest Neighbors (KNN)
    """
    def __init__(self, collaborative_model_trainer_config: CollaborativeModelConfig, data_transformation_artifact: DataTransformationArtifact):
        """
        Initializes the CollaborativeModelTrainer with configuration and transformed data.

        Args:
            collaborative_model_trainer_config (CollaborativeModelConfig): Configuration settings for model training.
            data_transformation_artifact (DataTransformationArtifact): Data artifact containing the preprocessed dataset path.
        """
        try:
            self.collaborative_model_trainer_config = collaborative_model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

    def initiate_model_trainer(self, model_type: str) -> CollaborativeModelArtifact:
        """
        Trains and saves the specified collaborative filtering model. 
        Args:
            model_type (str): The type of model to train. 
                              Choices: 'svd', 'item_knn', 'user_knn'.

        Returns:
            CollaborativeModelArtifact: Object containing the file path of the trained model. 
        """
        try:
            logging.info("Loading transformed data...")
            df = load_csv_data(self.data_transformation_artifact.merged_file_path)
            recommender = CollaborativeAnimeRecommender(df) 
            if model_type == 'svd':
                logging.info("Training and saving SVD model...")
                recommender.train_svd()
                save_model(recommender.svd, self.collaborative_model_trainer_config.svd_trained_model_file_path)

                logging.info("Loading pre-trained SVD model...")
                svd_model = load_object(self.collaborative_model_trainer_config.svd_trained_model_file_path)
                svd_recommendations = recommender.get_svd_recommendations(user_id=436, n=10, svd_model=svd_model)
                logging.info(f"SVD recommendations: {svd_recommendations}")
                return CollaborativeModelArtifact(
                    svd_file_path=self.collaborative_model_trainer_config.svd_trained_model_file_path
                )

            elif model_type == 'item_knn':
                logging.info("Training and saving KNN item-based model...")
                recommender.train_knn_item_based()
                save_model(recommender.knn_item_based, self.collaborative_model_trainer_config.item_knn_trained_model_file_path)

                logging.info("Loading pre-trained item-based KNN model...")
                item_knn_model = load_object(self.collaborative_model_trainer_config.item_knn_trained_model_file_path)
                item_based_recommendations = recommender.get_item_based_recommendations(
                    anime_name='One Piece', n_recommendations=10, knn_item_model=item_knn_model
                )
                logging.info(f"Item Based recommendations: {item_based_recommendations}")
                return CollaborativeModelArtifact(
                    item_based_knn_file_path=self.collaborative_model_trainer_config.item_knn_trained_model_file_path
                )

            elif model_type == 'user_knn':
                logging.info("Training and saving KNN user-based model...")
                recommender.train_knn_user_based()
                save_model(recommender.knn_user_based, self.collaborative_model_trainer_config.user_knn_trained_model_file_path)

                logging.info("Loading pre-trained user-based KNN model...")
                user_knn_model = load_object(self.collaborative_model_trainer_config.user_knn_trained_model_file_path)
                user_based_recommendations = recommender.get_user_based_recommendations(
                    user_id=817, n_recommendations=10, knn_user_model=user_knn_model
                )
                logging.info(f"User Based recommendations: {user_based_recommendations}")
                return CollaborativeModelArtifact(
                    user_based_knn_file_path=self.collaborative_model_trainer_config.user_knn_trained_model_file_path
                )

            else:
                raise ValueError("Invalid model_type. Choose from 'svd', 'item_knn', or 'user_knn'.")

        except Exception as e:
            raise AnimeRecommendorException(f"Error in CollaborativeModelTrainer: {str(e)}", sys)