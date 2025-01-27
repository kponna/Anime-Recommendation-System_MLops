import os
import sys
import time
import pandas as pd
import joblib
from anime_recommender.loggers.logging import logging
from anime_recommender.exception.exception import AnimeRecommendorException
from anime_recommender.constant import * 

def export_data_to_dataframe(dataframe: pd.DataFrame, file_path: str) -> pd.DataFrame:
        try:
            logging.info(f"Saving DataFrame to file: {file_path}")
            dir_path = os.path.dirname(file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(file_path, index=False, header=True)
            logging.info(f"DataFrame saved successfully to {file_path}.")
            return dataframe
        except Exception as e:
            raise AnimeRecommendorException(e, sys)

def load_csv_data(file_path: str) -> pd.DataFrame: 
    try:
        df = pd.read_csv(file_path)
        return df 
    except Exception as e:
        raise AnimeRecommendorException(e, sys) from e

def save_model(model: object,file_path: str ) -> None:
    try:
        logging.info("Entered the save_model method of Main utils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            joblib.dump(model, file_obj)
        logging.info("Completed saving the model object.")
    except Exception as e:
        raise AnimeRecommendorException(e, sys) from e
    
def load_object(file_path:str)-> object: 
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} is not exists")
        with open(file_path,"rb") as file_obj:
            print(file_obj)
            return joblib.load(file_obj)
    except Exception as e:
        raise AnimeRecommendorException(e,sys) from e
    